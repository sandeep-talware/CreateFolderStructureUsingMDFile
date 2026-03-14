#!/usr/bin/env python3

import os
import re
import argparse


TREE_PATTERN = re.compile(r"[├└]──\s+(.*)")


def extract_structure(md_file):
    """
    Extract only tree structure lines from markdown file
    """
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    structure_lines = []

    for line in lines:
        if "──" in line or line.strip().endswith("/"):
            structure_lines.append(line.rstrip())

    return structure_lines


def parse_tree(lines):
    """
    Parse tree lines into path list
    """
    stack = []
    paths = []

    for line in lines:

        if not line.strip():
            continue

        match = TREE_PATTERN.search(line)

        # Root folder
        if not match:
            name = line.strip()

            if name.endswith("/"):
                root = name.rstrip("/")
                stack = [root]
                paths.append(root + "/")

            continue

        name = match.group(1)

        indent = (len(line) - len(line.lstrip(" │"))) // 4

        while len(stack) > indent + 1:
            stack.pop()

        is_dir = name.endswith("/")
        clean_name = name.rstrip("/")

        stack.append(clean_name)

        path = os.path.join(*stack)

        if is_dir:
            path += "/"

        paths.append(path)

    return paths


def create_paths(paths, base_dir, dry_run=False):
    """
    Create directories and files
    """

    created_dirs = set()

    for path in paths:

        name = os.path.basename(path.rstrip("/"))

        # Skip hidden files/folders (.github, .mvn, .env, etc.)
        if name.startswith("."):
            print(f"[SKIP] hidden path: {path}")
            continue

        full_path = os.path.join(base_dir, path.rstrip("/"))

        is_dir = path.endswith("/")

        if dry_run:
            print("[DIR ]" if is_dir else "[FILE]", full_path)
            continue

        if is_dir:
            os.makedirs(full_path, exist_ok=True)
            created_dirs.add(full_path)

        else:
            os.makedirs(os.path.dirname(full_path), exist_ok=True)

            if not os.path.exists(full_path):
                open(full_path, "w").close()

    # Add .gitkeep to empty folders
    for directory in created_dirs:

        if os.path.isdir(directory) and not os.listdir(directory):
            gitkeep = os.path.join(directory, ".gitkeep")

            with open(gitkeep, "w") as f:
                f.write("")


def main():

    parser = argparse.ArgumentParser(
        description="Generate project folder structure from Markdown tree"
    )

    parser.add_argument(
        "markdown",
        help="Markdown file containing project structure",
    )

    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (default: same location as markdown)",
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview structure without creating files",
    )

    args = parser.parse_args()

    md_path = os.path.abspath(args.markdown)

    base_dir = args.output if args.output else os.path.dirname(md_path)

    # Ensure base directory exists
    os.makedirs(base_dir, exist_ok=True)

    lines = extract_structure(md_path)

    paths = parse_tree(lines)

    create_paths(paths, base_dir, args.dry_run)

    if not args.dry_run:
        print("\n✅ Project structure created successfully.")


if __name__ == "__main__":
    main()
