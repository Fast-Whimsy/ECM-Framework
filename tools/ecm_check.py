import os
import sys
import re

REQUIRED_DIRS = [
    "docs",
    "lineage",
    ".github/workflows",
]

REQUIRED_FILES = [
    "README.md",
    "lineage/lineage_notes.md",
]

# Robust patterns (allow leading whitespace)
README_VERSION_PATTERN = r"^\s*ECM Version:\s*v\d+\.\d+\.\d+"
README_CI_BADGE_PATTERN = r"actions/workflows/ci\.yml/badge\.svg"
README_LINEAGE_SECTION_PATTERN = r"^\s*##\s+Lineage\b"
README_INVARIANTS_SECTION_PATTERN = r"^\s*##\s+ECM Invariants\b"

ZERO_WIDTH = [
    "\ufeff",  # BOM
    "\u200b",  # zero-width space
    "\u200c",  # zero-width non-joiner
    "\u200d",  # zero-width joiner
    "\u2060",  # word joiner
    "\u00a0",  # non-breaking space
]

def fail(msg):
    print(f"[ECM CHECK FAILED] {msg}")
    sys.exit(1)

def check_dirs():
    for d in REQUIRED_DIRS:
        if not os.path.isdir(d):
            fail(f"Missing required directory: {d}")

def check_files():
    for f in REQUIRED_FILES:
        if not os.path.isfile(f):
            fail(f"Missing required file: {f}")

def check_ci():
    ci_path = ".github/workflows/ci.yml"
    if not os.path.isfile(ci_path):
        fail("Missing CI workflow at .github/workflows/ci.yml")

def load_and_normalize_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Strip BOM and zero-width characters
    for zw in ZERO_WIDTH:
        content = content.replace(zw, "")

    # Normalize line endings
    content = content.replace("\r\n", "\n").replace("\r", "\n")

    # Remove trailing spaces
    content = "\n".join(line.rstrip() for line in content.split("\n"))

    return content

def check_readme_version(content):
    if not re.search(README_VERSION_PATTERN, content, flags=re.MULTILINE):
        fail("README.md missing ECM version declaration (e.g., 'ECM Version: v0.1.0')")

def check_readme_ci_badge(content):
    if not re.search(README_CI_BADGE_PATTERN, content):
        fail("README.md missing CI badge pointing to .github/workflows/ci.yml")

def check_readme_lineage_section(content):
    if not re.search(README_LINEAGE_SECTION_PATTERN, content, flags=re.MULTILINE):
        fail("README.md missing '## Lineage' section")

def check_readme_invariants_section(content):
    if not re.search(README_INVARIANTS_SECTION_PATTERN, content, flags=re.MULTILINE):
        fail("README.md missing '## ECM Invariants' section")

def main():
    print("[ECM CHECK] Validating repository structure and README invariants...")

    check_dirs()
    check_files()
    check_ci()

    readme = load_and_normalize_readme()

    check_readme_version(readme)
    check_readme_ci_badge(readme)
    check_readme_lineage_section(readme)
    check_readme_invariants_section(readme)

    print("[ECM CHECK PASSED] Repository satisfies ECM structural and README invariants.")

if __name__ == "__main__":
    main()
