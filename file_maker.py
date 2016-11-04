from string import Template
import uuid

main_cmakefile = \
"""
cmake_minimum_required(VERSION 2.8)

project($project)

if(UNIX)
  set(CMAKE_CXX_FLAGS "$${CMAKE_CXX_FLAGS} -Wno-invalid-offsetof -g -std=c++11")
endif()

include_directories("$${CMAKE_CURRENT_SOURCE_DIR}/include")

add_subdirectory("src")

if(ENABLE_TEST)
  add_subdirectory(test)
endif()

install(DIRECTORY include/$project DESTINATION include)
"""

src_cmakefile = \
"""
set(PROJECT_NAME "$project")

FILE(GLOB_RECURSE all_files
*.cpp
*.cc
*.c++
*.c
*.C)

add_library($${PROJECT_NAME} STATIC $${all_files})

install(TARGETS $${PROJECT_NAME} ARCHIVE DESTINATION lib)
"""

test_cmakefile = \
"""
set(PROJECT_NAME "test_$project")

project($${PROJECT_NAME})

include_directories("$${CMAKE_CURRENT_SOURCE_DIR}/../include")

FILE(GLOB_RECURSE all_files
*.cpp
*.cc
*.c++
*.c
*.C)

add_executable($${PROJECT_NAME} $${all_files})
target_link_libraries($${PROJECT_NAME} $project)
"""

namespace_file = \
"""
#ifndef H$uuid
#define H$uuid

#define ${project_upper}_NS $project
#define ${project_upper}_NS_BEGIN namespace ${project_upper}_NS {
#define ${project_upper}_NS_END }
#define USING_${project_upper}_NS using namespace ${project_upper}_NS;
#define FWD_DECL_${project_upper}(type) namespace ${project_upper}_NS { struct type; }

#endif
"""

def make_cmake_file(project_name, template, file):
	s = Template(template)
	result = s.substitute(project = project_name)
	with open(file, 'w') as f:
		f.write(result)

def make_main_cmake_file(project_name, file):
	make_cmake_file(project_name, main_cmakefile, file)

def make_src_cmake_file(project_name, file):
	make_cmake_file(project_name, src_cmakefile, file)


def make_test_cmake_file(project_name, file):
	make_cmake_file(project_name, test_cmakefile, file)

def make_namespace_file(project_name, file):
	uuid_str = str(uuid.uuid1())
	include_guard = uuid_str.replace('-', '_').upper()
	s = Template(namespace_file)
	result = s.substitute(project = project_name, project_upper = project_name.upper(), uuid =  include_guard)
	with open(file, 'w') as f:
	    f.write(result)
