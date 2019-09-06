# MavenDependencyCheck
An automation Script to run [OWASP Dependency-Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) on Maven Based projects.

This script basically clones the given repositories and builds them using maven, once successful it runs dependency-check on them and generate the report

## Requirements
* Python modules: [os](https://docs.python.org/2/library/os.html) & [shutil](https://docs.python.org/2/library/shutil.html)
* Maven: Installation instructions can be found [here](https://maven.apache.org/install.html)
* [``` repo.conf```](https://github.com/security-prince/MavenDependencyCheck/blob/master/repo.conf) containing the git commands to be run for cloning the projects

Example commands for ```repo.conf```
 
 ```git clone https://github.com/elderstudios/uni-dvwa-spring.git```
 
## Usage
```python depcheck.py``` 

And let the script do the magic

##### Tested and working fine on CentOS Linux release 7.6.1810 (Core) with Python 2.7.5.

## Authors
* [Praveen Sutar](https://twitter.com/praveensutar123)
* [Ishaq Mohammed](https://twitter.com/security_prince)

## Credits
* [OWASP Dependency Check](https://www.owasp.org/index.php/OWASP_Dependency_Check) by [Jeremy Long](https://twitter.com/ctxt)
* [Shrutirupa Banerjiee](https://twitter.com/freak_crypt) & [Aishwarya Iyer](https://twitter.com/Aish_9524) for reviewing


