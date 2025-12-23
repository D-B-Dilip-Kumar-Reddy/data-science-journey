"""
Environment validation script.

Purpose:
- Verify Python version
- Verify critical packages are installed
- Ensure system is ready for data science work
"""

import sys

REQUIRED_PYTHON = (3, 9)


def check_python_version():
    if sys.version_info < REQUIRED_PYTHON:
        raise EnvironmentError(
            f"Python {REQUIRED_PYTHON[0]}.{REQUIRED_PYTHON[1]}+ required"
        )
    print("Python version OK")


def check_package(package_name):
    try:
        __import__(package_name)
        print(f"{package_name} installed")
    except ImportError:
        print(f"{package_name} NOT installed")


if __name__ == "__main__":
    check_python_version()

    for pkg in ["numpy", "pandas", "pytest"]:
        check_package(pkg)
