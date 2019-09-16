#!/usr/bin/python
# Project : MavenDependencyCheck
#Description: An automation Script to run OWASP Dependency-Check on Maven Based projects.
# Version : 1.5
# Authors" Praveen Sutar & Ishaq Mohammed

import os
import shutil

def init_pull():
    "Downloads Dependency-check and creates directories"
    report_dir = "depcheckreports"
    project_dir = "projects"
    dependecy_ckeck_launcher = "dependency-check"
    if not os.path.exists(report_dir):
        print "## The result directory not present so creating directory"
        os.makedirs(report_dir)
    if not os.path.exists(project_dir):
        print "## The project directory not present so creating directory for project repository"
        os.makedirs(project_dir)
    if not os.path.exists(dependecy_ckeck_launcher):
        print "## The dependency_check_launcher directory not present , pulling launcher"
        launcher_pull = "wget https://dl.bintray.com/jeremy-long/owasp/dependency-check-5.2.1-release.zip"
        os.system(launcher_pull)
        unzip_launcher = "unzip dependency-check-5.2.1-release.zip"
        os.system(unzip_launcher)

def read_conf():
    "Runs the git commands from the repo.conf file to clone the projects"
    with open('repo.conf') as f:
        for line in f:
            print line
            linevar = " " + line
            os.chdir("./projects/")
            os.system('%s' % linevar)
            print "## Repo pulled successfully"
            os.chdir("../")

def launcher():
    "Pulling the latest repo and building the project using mvn"
    laucher_path = "dependency-check/bin/dependency-check.sh"
    os.chdir("./projects/")
    print "#### Pulling git for latest repo and building the project using maven"
    os.system(
        'for i in */.git; do ( echo $i; cd $i/..; git pull; mvn clean install -DskipTests=true ;); done')
    print "## Latest Repo Pulled successfully"
    os.chdir("../")
    report_dir = "result"
    os.system('ls ./projects/ > project_name.txt')
    with open('project_name.txt') as p:
        for pname in p:
            print pname
            project_path = "./projects/" + pname
            result_path = "./depcheckreports/" + pname
            print "#### launching Dependency Check ..."
            os.system('bash dependency-check/bin/dependency-check.sh --project test --disableNodeAudit --disableNodeJS --format ALL -s %s ' % project_path)

            #Moving the reports to depcheckreports directory
            extlists=['.csv','.html','.xml','.json']
            for ext in extlists:
                src = "dependency-check-report" + ext
                dst = "./depcheckreports/" + pname.strip() + ext
                shutil.move(src, dst)

def main():
    init_pull()
    read_conf()
    launcher()

if __name__ == "__main__":
    main()

