#!/usr/bin/env python3
"""
Version management script for openphone-python.

Usage:
    python scripts/version.py                    # Show current version
    python scripts/version.py get               # Show current version
    python scripts/version.py patch             # Bump patch version
    python scripts/version.py minor             # Bump minor version
    python scripts/version.py major             # Bump major version
    python scripts/version.py set 1.2.3         # Set specific version
"""

import sys
import re
from pathlib import Path


def get_version_file():
    """Get the path to the version file."""
    return Path(__file__).parent.parent / "src" / "openphone_python" / "_version.py"


def read_version():
    """Read the current version from _version.py."""
    version_file = get_version_file()
    content = version_file.read_text()
    match = re.search(r'__version__ = ["\']([^"\']+)["\']', content)
    if not match:
        raise ValueError("Could not find version in _version.py")
    return match.group(1)


def write_version(new_version):
    """Write a new version to _version.py."""
    version_file = get_version_file()
    content = version_file.read_text()

    # Update __version__
    content = re.sub(
        r'__version__ = ["\'][^"\']+["\']',
        f'__version__ = "{new_version}"',
        content
    )

    version_file.write_text(content)
    print(f"Updated version to {new_version}")


def parse_version(version_str):
    """Parse a version string into major, minor, patch."""
    parts = version_str.split(".")
    if len(parts) != 3:
        raise ValueError("Version must be in format MAJOR.MINOR.PATCH")

    try:
        return tuple(int(part) for part in parts)
    except ValueError:
        raise ValueError("Version parts must be integers")


def bump_version(bump_type):
    """Bump the version by the specified type."""
    current = read_version()
    major, minor, patch = parse_version(current)

    if bump_type == "major":
        major += 1
        minor = 0
        patch = 0
    elif bump_type == "minor":
        minor += 1
        patch = 0
    elif bump_type == "patch":
        patch += 1
    else:
        raise ValueError("Bump type must be 'major', 'minor', or 'patch'")

    new_version = f"{major}.{minor}.{patch}"
    write_version(new_version)
    return new_version


def main():
    """Main script entry point."""
    if len(sys.argv) == 1:
        # Show current version
        print(f"Current version: {read_version()}")
        return

    command = sys.argv[1]

    if command == "get":
        # Show current version
        print(f"Current version: {read_version()}")
    elif command in ["major", "minor", "patch"]:
        new_version = bump_version(command)
        print(f"Bumped {command} version to {new_version}")
    elif command == "set":
        if len(sys.argv) != 3:
            print("Usage: python scripts/version.py set VERSION")
            sys.exit(1)

        new_version = sys.argv[2]
        # Validate version format
        parse_version(new_version)
        write_version(new_version)
        print(f"Set version to {new_version}")
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
