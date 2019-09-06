# DepCheck
An automation Script to run [OWASP Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) on Maven Based projects
This script basically clones the given repositories and builds them using maven, once successful it runs dependency-check on them and generate the report

# Requirements
* Python modules: [os](https://docs.python.org/2/library/os.html) & [shutil](https://docs.python.org/2/library/shutil.html)
* Maven Installed: Instructions for installing maven can be found [here](https://maven.apache.org/install.html)
* ``` repo.conf``` containing the git commands to be run for cloning the projects
Example command for '''repo.conf'''

```git clone https://github.com/elderstudios/uni-dvwa-spring.git
   git clone https://github.com/CSPF-Founder/VulnerableSpring.git ```


