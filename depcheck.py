#!/usr/bin/python
# Project : MavenDependencyCheck
# Description: An automation Script to run OWASP Dependency-Check on Maven Based projects.
# Version : 1.5
# Authors" Praveen Sutar & Ishaq Mohammed


import os
import shutil
import subprocess

from lib import constants, helpers
from lib.helpers import download_dependency_check_tool


def init_pull():
    """Downloads Dependency-check and creates directories"""
    if os.path.exists(constants.DEPENDENCY_CHECK_TOOL):
        version = (
            subprocess.check_output(
                [constants.DEPENDENCY_CHECK_TOOL, "--version"]
            )
            .decode("utf-8")
            .split(" ")[-1]
        )
        download_dependency_check_tool(old_version=version)
    else:
        download_dependency_check_tool()

    if not os.path.exists(constants.REPORT_DIR):
        print("[INFO]: The result directory not present so creating directory")
        os.makedirs(constants.REPORT_DIR)

    if not os.path.exists(constants.PROJECTS_DIR):
        print(
            "[INFO]: The project directory not present so creating directory for project repository"
        )
        os.makedirs(constants.PROJECTS_DIR)


def read_conf():
    """Runs the git commands from the repo.conf file to clone the projects"""
    with open(constants.CONFIG_FILE) as f:
        for line in f:
            if line.startswith("git"):
                print(line.replace("\n", ""))
                commands = line.replace("\n", "").split(" ")
                repo_name = os.path.splitext(
                    commands[-1].split("/")[-1].split("\\")[-1]
                )[0]
                if os.path.exists(constants.PROJECTS_DIR / repo_name):
                    shutil.rmtree(constants.PROJECTS_DIR / repo_name, onexc=helpers.onexec)
                helpers.run_command(
                    command_list=[
                        *commands,
                        str(constants.PROJECTS_DIR / repo_name),
                    ]
                )


def launcher():
    """Pulling the latest repo and building the project using mvn"""

    for dirpath, _, filenames in os.walk(
        constants.PROJECTS_DIR, topdown=False
    ):
        if "pom.xml" in filenames:
            os.chdir(dirpath)
            project_name = os.path.splitext(
                dirpath.split("/")[-1].split("\\")[-1]
            )[0]
            report_path = constants.REPORT_DIR / project_name
            os.makedirs(report_path, exist_ok=True)

            pull_command = "git pull"
            helpers.run_command(
                command_list=pull_command.split(" "), shell=True
            )

            mvn_command = "mvn clean install -DskipTests=true"
            helpers.run_command(
                command_list=mvn_command.split(" "), shell=True
            )

            # dependency_check_command = f'''{constants.DEPENDENCY_CHECK_TOOL}\
            # --project "{project_name}" --format "ALL" --enableExperimental --enableRetired\
            # --disableAssembly --disableYarnAudit --prettyPrint --out "{report_path}" --scan "{dirpath}"\
            # --proxyserver "proxy.company.com" --proxyport 8080 --proxyuser "user" --proxypass "pass"'''

            dependency_check_command = f'''{constants.DEPENDENCY_CHECK_TOOL}\
            --project "{project_name}" --format "ALL" --enableExperimental\
            --enableRetired --disableAssembly --disableYarnAudit --prettyPrint\
            --out "{report_path}" --scan "{dirpath}"'''

            if os.environ.get("NVD_API_KEY"):
                dependency_check_cmd = [
                    *dependency_check_command.split(" "),
                    "--nvdApiKey",
                    os.environ.get("NVD_API_KEY"),
                ]
                print(f"[INFO] running command: {" ".join([item for item in dependency_check_cmd if item])}")
                helpers.run_command(
                    [item for item in dependency_check_cmd if item],
                    shell=True,
                )
            else:
                print(f"[INFO] running command: {" ".join([item for item in dependency_check_command.split(" ") if item])}")
                helpers.run_command(
                    [
                        item
                        for item in dependency_check_command.split(" ")
                        if item
                    ],
                    shell=True,
                )


def main():
    init_pull()
    read_conf()
    launcher()


if __name__ == "__main__":
    main()
