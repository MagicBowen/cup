import os
import file_maker

def touch_file(path):
	open(path, 'w').close()

def new_cmd(args):
	project = args.project


	projectPath = os.path.join(os.getcwd(), project)

	assert not(os.path.exists(projectPath))

	os.makedirs(projectPath)

	os.makedirs(os.path.join(projectPath, "include/" + project))
	os.makedirs(os.path.join(projectPath, "src"))
	os.makedirs(os.path.join(projectPath, "test"))
	os.makedirs(os.path.join(projectPath, "deps"))
	os.makedirs(os.path.join(projectPath, "docs"))

	main_cmake_file = projectPath + "/CMakeLists.txt"
	src_cmake_file = projectPath + "/src/" + "CMakeLists.txt"
	test_cmake_file = projectPath + "/test/" + "CMakeLists.txt"
	include_file = projectPath + "/include/" + project + "/" + project + ".h"

	touch_file(include_file)
	touch_file(main_cmake_file)
	touch_file(src_cmake_file)
	touch_file(test_cmake_file)
	touch_file(projectPath + "/deps/" + "deps.toml")
	touch_file(projectPath + "/docs/" + project + ".md")
	touch_file(projectPath + "/" + project +".toml")

	file_maker.make_main_cmake_file(project, main_cmake_file)
	file_maker.make_src_cmake_file(project, src_cmake_file)
	file_maker.make_test_cmake_file(project, test_cmake_file)
	file_maker.make_namespace_file(project, include_file)
