# CUP : C++ unified package management tool

[https://magicbowen.github.io/cup/](https://magicbowen.github.io/cup/)

## install

- download cup source code
- be sure python3 installed on your machine
- be sure cmake installed on your machine
- for windows: add cup folder to you environment variable ‘path’
- for linux or mac:

~~~bash
sudo ln -s /path/to/your/cup.py /usr/local/bin/cup
~~~

check whether cup installed successful

~~~bash
cup -h
~~~

## usage

### create project

Below we create a cpp project named 'cppcon' in testcup folder.

~~~bash
mkdir testcup
cd testcup
cup new cppcon
~~~

If you want cup to generate the eclipse project, add '-e'. 
If you want cup to generate the default build script, add '-b'

~~~bash
cup new cppcon -e -b
~~~

### add file

~~~bash
# add a header file
cup add include/cppcon/Header.h -i

# add a source file
cup add src/Source.cpp -s

# add a test file
cup add test/TestSource.cpp -t

# add a class with header and source files
cup add src/Object -c

# add a class with header, source and test files
cup add src/Object -a

# could add files in any project sub folder
cd include/cppcon
cup add subfolder/Object2 -a
~~~

### build

~~~bash
cup build
~~~

~~~bash
cup build --clean
~~~

### test

~~~bash
cup test
~~~

you can also run build and test through build script generated when project created

## config

### modify file template

All file template in '.cup/templates', you can change the file template of header, source and test.

### modify build parameters

- modify the build script generated when project created
- or, modify the config file in '.cup/config' (will give details later)

### modify test framework

- cup uses gtest for default, add 'GTEST_HOME' to your environment variable 
- make sure 'GTEST_HOME' include the folder 'gtest/include' and 'lib/libgtest.a'

if you want to change the test framework setting:

- directly modify the CMakeLists.txt in test folder
- modify the 'test/main.cpp' and test template
- or you can modify the config in '.cup/config' (will give details later)

