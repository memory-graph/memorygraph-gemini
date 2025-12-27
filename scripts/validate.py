#!/usr/bin/env python3
"""Validation script for memorygraph-gemini extension."""

import json
import sys
import tomllib
from pathlib import Path

def validate_json(file_path: Path) -> list[str]:
    """Validate JSON file syntax."""
    errors = []
    try:
        with open(file_path) as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"{file_path}: JSON syntax error - {e}")
    except Exception as e:
        errors.append(f"{file_path}: Error reading file - {e}")
    return errors

def validate_toml(file_path: Path) -> list[str]:
    """Validate TOML file syntax."""
    errors = []
    try:
        with open(file_path, "rb") as f:
            data = tomllib.load(f)
        # Check required fields
        if "description" not in data:
            errors.append(f"{file_path}: Missing 'description' field")
        if "prompt" not in data:
            errors.append(f"{file_path}: Missing 'prompt' field")
    except tomllib.TOMLDecodeError as e:
        errors.append(f"{file_path}: TOML syntax error - {e}")
    except Exception as e:
        errors.append(f"{file_path}: Error reading file - {e}")
    return errors

def validate_manifest(file_path: Path) -> list[str]:
    """Validate gemini-extension.json manifest."""
    errors = []
    try:
        with open(file_path) as f:
            data = json.load(f)

        # Required fields
        required = ["name", "version", "mcpServers"]
        for field in required:
            if field not in data:
                errors.append(f"{file_path}: Missing required field '{field}'")

        # Validate mcpServers structure
        if "mcpServers" in data:
            for name, config in data["mcpServers"].items():
                if "command" not in config:
                    errors.append(f"{file_path}: MCP server '{name}' missing 'command'")

    except json.JSONDecodeError as e:
        errors.append(f"{file_path}: JSON syntax error - {e}")
    return errors

def main():
    """Run all validations."""
    root = Path(__file__).parent.parent
    all_errors = []

    print("Validating memorygraph-gemini extension...\n")

    # Validate manifest
    manifest = root / "gemini-extension.json"
    if manifest.exists():
        print(f"✓ Checking {manifest.name}")
        all_errors.extend(validate_manifest(manifest))
    else:
        all_errors.append("gemini-extension.json not found!")

    # Validate package.json
    package = root / "package.json"
    if package.exists():
        print(f"✓ Checking {package.name}")
        all_errors.extend(validate_json(package))

    # Validate TOML command files
    commands_dir = root / "commands" / "memory"
    if commands_dir.exists():
        for toml_file in commands_dir.glob("*.toml"):
            print(f"✓ Checking {toml_file.relative_to(root)}")
            all_errors.extend(validate_toml(toml_file))

    # Summary
    print()
    if all_errors:
        print(f"❌ Found {len(all_errors)} error(s):\n")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print("✅ All validations passed!")
        sys.exit(0)

if __name__ == "__main__":
    main()
