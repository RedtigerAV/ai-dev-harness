#!/usr/bin/env python3
"""Offline maintainer checks; never installs or configures a target repository."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required for this maintainer check; use an isolated environment.")


class UniqueKeysLoader(yaml.SafeLoader):
    """Reject silent YAML key replacement."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node)
    return result


UniqueKeysLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping
)
ROOT = Path(__file__).resolve().parents[1]
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def load_yaml(path):
    return yaml.load(path.read_text(), Loader=UniqueKeysLoader)


def local_path(source, reference):
    target = (source.parent / unquote(urlsplit(reference).path)).resolve()
    check(target.is_relative_to(ROOT), f"{source.relative_to(ROOT)}: path escapes repo: {reference}")
    check(target.exists(), f"{source.relative_to(ROOT)}: missing local path: {reference}")
    return target


def check_catalog(filename):
    path = ROOT / "registry" / filename
    catalog = load_yaml(path)
    check(catalog.get("schema_version") == 1, f"{filename}: unsupported schema")
    check(bool(catalog.get("reviewed_on")), f"{filename}: missing review date")
    components = catalog["components"]
    ids = [entry["id"] for entry in components]
    check(len(ids) == len(set(ids)), f"{filename}: duplicate IDs")
    for entry in components:
        label = f"{filename}/{entry['id']}"
        check(bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["id"])), f"{label}: invalid ID")
        for field in ("name", "description", "source", "recommend_for", "caveats", "verify"):
            check(bool(entry.get(field)), f"{label}: missing {field}")
        check(type(entry.get("required")) is bool, f"{label}: required must be boolean")
        check(urlsplit(entry["source"]).scheme == "https", f"{label}: source must use HTTPS")
        if filename == "skills.yaml":
            usage = entry.get("usage", {})
            if not isinstance(usage, dict):
                check(False, f"{label}: usage must be a mapping")
                usage = {}
            check(usage.get("role") in ("workflow", "domain", "diagnostic"), f"{label}: invalid usage role")
            for field in ("contexts", "when", "when_not"):
                values = usage.get(field)
                valid_list = isinstance(values, list) and all(
                    isinstance(value, str) and value.strip() for value in values
                )
                # A skill need not invent exclusions when none apply.
                check(
                    valid_list and (field == "when_not" or bool(values)),
                    f"{label}: usage.{field} must be a string list"
                    + (" (may be empty)" if field == "when_not" else " with at least one item"),
                )
            check(
                isinstance(usage.get("instruction"), str) and bool(usage["instruction"].strip()),
                f"{label}: missing usage instruction",
            )
            install = entry["install"]
            check(bool(install.get("selection")), f"{label}: missing selection boundary")
            check(bool(install.get("method")), f"{label}: missing install method")
            for field in ("path", "guide"):
                if field in install:
                    local_path(ROOT / "README.md", install[field])
            if entry["kind"] == "custom-skill":
                check((ROOT / install["path"] / "SKILL.md").is_file(), f"{label}: missing skill")
        else:
            for field in ("prerequisites", "authentication", "scope"):
                check(bool(entry.get(field)), f"{label}: missing {field}")
            transport = entry["transport"]
            check(transport in ("http", "stdio"), f"{label}: unknown transport")
            if transport == "http":
                check(urlsplit(entry.get("endpoint", "")).scheme == "https", f"{label}: invalid endpoint")
            if transport == "stdio":
                launch = entry["launch"]
                check(bool(launch.get("command")), f"{label}: missing command")
                check(isinstance(launch.get("args"), list), f"{label}: args must be a list")
    return components


def main():
    skills = check_catalog("skills.yaml")
    mcps = check_catalog("mcp.yaml")
    required = [entry["id"] for entry in skills + mcps if entry["required"]]
    check(required == ["superpowers"], "Only Superpowers is the required foundation")
    all_ids = [entry["id"] for entry in skills + mcps]
    check(len(all_ids) == len(set(all_ids)), "Catalog IDs must be globally unique")

    record = load_yaml(ROOT / "templates/installation-record.yaml")
    check(record["schema_version"] == 1, "Record schema differs from documented version")
    for entry in record["components"]:
        check(entry["id"] in all_ids, "Record example refers to an unknown component")
        check(entry["state"] == "requested", "Record template must not claim installation")
        check(not entry["observation"]["evidence"], "Template must not invent evidence")

    for skill in (ROOT / "skills").glob("*/SKILL.md"):
        match = re.match(r"\A---\n(.*?)\n---\n", skill.read_text(), re.S)
        check(match is not None, f"{skill}: missing frontmatter")
        if match:
            metadata = yaml.load(match[1], Loader=UniqueKeysLoader)
            check(metadata.get("name") == skill.parent.name, f"{skill}: name mismatch")
            check(bool(metadata.get("description")), f"{skill}: empty description")

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        # Repository links use inline Markdown. URLs and fragment-only links are external to this check.
        for reference in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", markdown.read_text()):
            if urlsplit(reference).scheme or reference.startswith("#"):
                continue
            target = local_path(markdown, reference)
            if markdown.is_relative_to(ROOT / "skills"):
                skill_root = ROOT / "skills" / markdown.relative_to(ROOT / "skills").parts[0]
                check(target.is_relative_to(skill_root), f"{markdown}: non-portable skill reference")

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"PASS: {len(skills)} skill entries, {len(mcps)} MCP entries, record template, skill metadata and local links.")
    print("Static checks only; client discovery, authentication and agent behavior require live verification.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyError, TypeError, ValueError, yaml.YAMLError) as error:
        sys.exit(f"ERROR: Invalid repository metadata: {error}")
