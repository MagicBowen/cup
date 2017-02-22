# CUP 

C++ unified package management tool (v0.1)

---

## Introduction

CUP is a command line tool to simplify the C++ project management.

---

## install

- download cup source code
- be sure python3 installed on your machine
- be sure cmake installed on your machine

--- 

## Windows install

add cup folder to you environment variable ‘path’

---

## Linux or Mac install

~~~bash
sudo ln -s /path/to/your/cup.py /usr/local/bin/cup
~~~

---

## usage

~~~bash
cup -h
~~~

---

## create project

~~~bash
# create a cpp project named 'cppcon' in testcup folder.

mkdir testcup
cd testcup
cup new cppcon
~~~

---

If you want to generate the eclipse project, add '-e'. 
If you want to generate the default build script, add '-b'

~~~bash
cup new cppcon -e -b
~~~

---

## add file

~~~bash
# add a header file
cup add include/cppcon/Header.h -i

# add a source file
cup add src/Source.cpp -s

# add a test file
cup add test/TestSource.cpp -t
~~~

---

## add class

~~~bash
# add a class with header and source files
cup add src/Object -c

# add a class with header, source and test files
cup add src/Object -a

# could add files in any project sub folder
cd include/cppcon
cup add subfolder/Object2 -a
~~~

---

## build

~~~bash
cup build
~~~

~~~bash
cup build --clean
~~~

---

## test

~~~bash
cup test
~~~

---

you can also run build and test through build script generated when project created

~~~bash
# make sure generated project with '-b' to create the build script
chmod a+x build.sh
./build.sh
~~~

---

## eclipse project

if you generated eclipse project when project generated ('-e'),
you can import the project to eclipse directly.

---

## modify file template

All file template in '.cup/templates' under project folder, 
you can change the file template of header, source and test.

---

## modify build parameters

- modify the build script generated when project created
- or, modify the config file in '.cup/config' (will give details later)

---

## modify test framework settings

- cup uses gtest for default, add 'GTEST_HOME' to your environment variable 
- make sure 'GTEST_HOME' include the folder 'gtest/include' and 'lib/libgtest.a'

---

## change test framework

- directly modify the CMakeLists.txt in test folder
- modify the 'test/main.cpp' and test template
- or you can modify the config in '.cup/config' (will give details later)

---

## future features

- support more project level and global level configurations for build and test
- refactoring: rename heade file, rename class, move header file, move folder
- package dependency government
- file level dependency government

