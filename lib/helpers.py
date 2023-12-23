import io
import os
import subprocess
from zipfile import ZipFile

import requests
from packaging.version import parse as versionParse

from lib import constants


def onexec(func, path, exc_info):
    """

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.
    """
    import stat

    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise


def run_command(command_list, shell=False):
    """runs the command in shell

    Args:
        command_list (list): list of words of command
        Ex: git clone repo_url --> ["git", "clone" "repo_url"]
    """
    process = subprocess.Popen(
        command_list, stdout=subprocess.PIPE, shell=shell
    )

    for data in io.TextIOWrapper(process.stdout, encoding="utf-8"):
        print(data)


def download_dependency_check_tool(old_version="0.0.0"):
    """Downloads Latest Dependency Check Tool from website on runtime

    Args:
        old_version (str): version dependency check tool if it is present in user system
    """

    new_version = requests.get(
        constants.DEPENDENCY_CHECK_LATEST_VERSION_CHECK_URL
    ).text

    if versionParse(old_version) < versionParse(new_version):
        print(
            "[INFO]: Your System Don't Have Dependency-check Tool Or Present Lower Version Than Latest Verion."
        )
        print(f"[INFO]: Your System Tool Version: {old_version}")
        print(f"[INFO]: Latest Tool Version Present In Web: {new_version}")

        resopnse = requests.get(
            constants.DEPENDENCY_CHECK_DOWNLOAD_URL.format(version=new_version)
        )

        if resopnse.ok:
            with ZipFile(io.BytesIO(resopnse.content)) as zf:
                zf.extractall(constants.ROOT_DIR)
        print("[INFO]: Download Completed.")
        print("[INFO]: Scan will Initiated.")
    else:
        print(
            "[INFO]: Your System Conatins Latest Version Of Dependency-check Tool."
        )
        print("[INFO]: Scan will Initiated.")
