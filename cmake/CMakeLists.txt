cmake_minimum_required(VERSION 2.8)

include("source-group.cmake")

project(${proj_name})

include_directories( 
"${CMAKE_CURRENT_SOURCE_DIR}/include"
)

if(MSVC)
    add_definitions(-D_CRT_SECURE_NO_WARNINGS)
    add_definitions(-DMSVC_VMG_ENABLED)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} /vmg")
endif(MSVC)

if(UNIX)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
endif(UNIX)

file(GLOB_RECURSE all_files 
include/*.h
include/*.hpp
include/*.hxx
include/*.tcc
src/*.cpp
src/*.cc
src/*.cxx
src/*.c
src/*.C
test/*.h
test/*.hpp
test/*.hxx
test/*.tcc
test/*.cpp
test/*.cc
test/*.cxx
test/*.c
test/*.C)

assign_source_group(all_files)

# link_directories("${CMAKE_CURRENT_SOURCE_DIR}/3th/lib")

# set(CMAKE_BUILD_TYPE ${CMAKE_BUILD_TYPE})

add_executable(${proj_name} ${all_files})

# target_link_libraries(${proj_name} gtest-vc80)