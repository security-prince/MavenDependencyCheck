import os
from pathlib import Path
from platform import system

DEPENDENCY_CHECK_LATEST_VERSION_CHECK_URL = (
    "https://jeremylong.github.io/DependencyCheck/current.txt"
)

DEPENDENCY_CHECK_DOWNLOAD_URL = (
    "https://github.com/jeremylong/DependencyCheck/releases/download/"
    "v{version}/dependency-check-{version}-release.zip"
)
ROOT_DIR = Path().resolve(__file__)

REPORT_DIR = ROOT_DIR / "depcheckreports"
PROJECTS_DIR = ROOT_DIR / "projects"
DEPENDENCY_CHECK_TOOL = os.path.join(
    ROOT_DIR,
    "dependency-check",
    "bin",
    "dependency-check.bat"
    if system().lower() == "windows"
    else "dependency-check.sh",
)
CONFIG_FILE = ROOT_DIR / "repo.conf"
