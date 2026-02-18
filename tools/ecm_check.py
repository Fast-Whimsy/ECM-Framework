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

README_VERSION_PATTERN = r"ECM Version:\s*v\d+\.\d+\.\d+"
README_CI_BADGE_PATTERN = r"actions/workflows/ci\.yml/badge\.svg"
README_LINEAGE_SECTION_PATTERN = r"^##\s+Lineage\b"
README_INVARIANTS_SECTION_PATTERN = r"^##\s+ECM Invariants\b"

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

def load_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

def check_readme_version(content: str):
    if not re.search(README_VERSION_PATTERN, content):
        fail("README.md missing ECM version declaration (e.g., 'ECM Version: v0.1.0')")

def check_readme_ci_badge(content: str):
    if not re.search(README_CI_BADGE_PATTERN, content):
        fail("README.md missing CI badge pointing to .github/workflows/ci.yml")

def check_readme_lineage_section(content: str):
    if not re.search(README_LINEAGE_SECTION_PATTERN, content, flags=re.MULTILINE):
        fail("README.md missing '## Lineage' section")

def check_readme_invariants_section(content: str):
    if not re.search(README_INVARIANTS_SECTION_PATTERN, content, flags=re.MULTILINE):
        fail("README.md missing '## ECM Invariants' section")

def main():
    print("[ECM CHECK] Validating repository structure and README invariants...")
    check_dirs()
    check_files()
    check_ci()

    readme = load_readme()
    check_readme_version(readme)
    check_readme_ci_badge(readme)
    check_readme_lineage_section(readme)
    check_readme_invariants_section(readme)

    print("[ECM CHECK PASSED] Repository satisfies ECM structural and README invariants.")

if __name__ == "__main__":
    main()
