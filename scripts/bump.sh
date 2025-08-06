#!/bin/bash
"""
Version management helper script for openphone-python.

This script provides easy commands for version management:
  ./scripts/bump.sh patch    # Bump patch version (0.1.0 -> 0.1.1)
  ./scripts/bump.sh minor    # Bump minor version (0.1.0 -> 0.2.0)
  ./scripts/bump.sh major    # Bump major version (0.1.0 -> 1.0.0)
  ./scripts/bump.sh set X.Y.Z # Set specific version
"""

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${YELLOW}OpenPhone Python SDK - Version Manager${NC}"
echo "============================================"

# Check if we're in the right directory
if [ ! -f "$PROJECT_DIR/pyproject.toml" ]; then
    echo -e "${RED}Error: Not in project root directory${NC}"
    exit 1
fi

# Function to show current version
show_version() {
    echo -e "${GREEN}Current version:${NC}"
    uv run python scripts/version.py
}

# Function to bump version
bump_version() {
    local bump_type=$1
    echo -e "${GREEN}Bumping ${bump_type} version...${NC}"

    # Bump the version
    uv run python scripts/version.py "$bump_type"

    # Show new version
    echo -e "${GREEN}New version:${NC}"
    uv run python scripts/version.py

    # Optionally commit the change
    read -p "Commit version bump? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        new_version=$(uv run python scripts/version.py get | sed 's/Current version: //')
        git add src/openphone_python/_version.py
        git commit -m "bump: version $new_version"
        echo -e "${GREEN}Version bump committed!${NC}"

        # Optionally create a tag
        read -p "Create git tag? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git tag "v$new_version"
            echo -e "${GREEN}Created tag v$new_version${NC}"
            echo "Push with: git push origin v$new_version"
        fi
    fi
}

# Function to set specific version
set_version() {
    local version=$1
    echo -e "${GREEN}Setting version to $version...${NC}"

    uv run python scripts/version.py set "$version"

    echo -e "${GREEN}Version set to $version${NC}"
}

# Main logic
case "${1:-show}" in
    "show"|"")
        show_version
        ;;
    "patch"|"minor"|"major")
        bump_version "$1"
        ;;
    "set")
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Version required for 'set' command${NC}"
            echo "Usage: $0 set X.Y.Z"
            exit 1
        fi
        set_version "$2"
        ;;
    "help"|"-h"|"--help")
        echo "$0"
        echo ""
        echo "Commands:"
        echo "  show         Show current version (default)"
        echo "  patch        Bump patch version (X.Y.Z -> X.Y.Z+1)"
        echo "  minor        Bump minor version (X.Y.Z -> X.Y+1.0)"
        echo "  major        Bump major version (X.Y.Z -> X+1.0.0)"
        echo "  set X.Y.Z    Set specific version"
        echo "  help         Show this help"
        ;;
    *)
        echo -e "${RED}Error: Unknown command '$1'${NC}"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac
