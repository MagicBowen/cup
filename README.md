# CUP : C++ unified package management tool

## usage

~~~bash
mkdir testcup
cd testcup
python cup.py init testcup
python cup.py new -a Example
chmod a+x build.sh
./build.sh
~~~

after create a project, you can import the project to eclipse-cdt directly.


## to to

- [x]: create a new project, create the default folders and files
- [x]: generate file: header file, source file, test file, class, and class with test
- [x]: generate the build script for linux/mac
- [x]: generate the build script for windows
- [x]: generate the eclipse project files

- [x]: generate file in subfolder for project

- [ ]: rename a class
- [ ]: rename a header file
- [ ]: move a header file
- [ ]: move a header folder

- [ ]: update the test setting by config file
- [ ]: update the build attributes by config file
- [ ]: recover a project by project cup config file

- [ ]: can gerarate the git repo for package and gitignore (ignore eclipse and build)

- [ ]: can describe the dependent package in local
- [ ]: can describe the dependent package in git by commit id
- [ ]: can decide to copy the dependent to project or not
- [ ]: can describe the dependent by a remote git repo and download to local
- [ ]: can check the complicated dependences, check the duplicated depend and ring depend
- [ ]: can publish project
- [ ]: can auto recognize the dependent files by '#include'
- [ ]: just download the dependent files
