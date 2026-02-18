import os
import sys
import re

REQUIRED_DIRS = [
    "docs",
    "lineage",
    ".github/workflows"
]

REQUIRED_FILES = [
    "README.md",
    "lineage/lineage_notes.md",
]

README_VERSION_PATTERN = r"ECM Version:\s*v\d+\.\d+\.\d+"

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

def check_readme_version():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    if not re.search(README_VERSION_PATTERN, content):
        fail("README.md missing ECM version declaration (e.g., 'ECM Version: v0.1.0')")

def main():
    print("[ECM CHECK] Validating repository structure...")
    check_dirs()
    check_files()
    check_ci()
    check_readme_version()
    print("[ECM CHECK PASSED] Repository satisfies ECM structural requirements.")

if __name__ == "__main__":
    main()
