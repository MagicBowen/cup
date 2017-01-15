import os
from string import Template
from fileutils import FileUtils


class CupInfo:
    template_files = {'project_config'  : 'project.cup.template',
                     'project_cmake'    : 'project.cmake.template',
                     'build_sh'         : 'project.build.sh.template',
                     'build_bat'        : 'project.build.bat.template',
                     'eclipse_project'  : 'eclipse.project.template',
                     'eclipse_cproject' : 'eclipse.cproject.template',
                     'namespace'        : 'project.h.template',
                     'src_cmake'        : 'src.cmake.template',
                     'test_cmake'       : 'test.cmake.template',
                     'test_main'        : 'test.main.cpp.template',
                     'header_file'      : 'struct.h.template',
                     'src_file'         : 'struct.cpp.template',
                     'test_file'        : 'test.struct.cpp.template'}

    target_files =   {'project_config'  : '${project_root}/${project}.cup',
                     'project_cmake'    : '${project_root}/CMakeLists.txt',
                     'build_sh'         : '${project_root}/build.sh',
                     'build_bat'        : '${project_root}/build.bat',
                     'eclipse_project'  : '${project_root}/.project',
                     'eclipse_cproject' : '${project_root}/.cproject',
                     'namespace'        : '${project_root}/include/${project}/${project}.h',
                     'src_cmake'        : '${project_root}/src/CMakeLists.txt',
                     'test_cmake'       : '${project_root}/test/CMakeLists.txt',
                     'test_main'        : '${project_root}/test/main.cpp',
                     'header_file'      : '${project_root}/include/${project}/${filepath}/${filename}',
                     'src_file'         : '${project_root}/src/${filepath}/${filename}',
                     'test_file'        : '${project_root}/test/${filepath}/${filename}'}

    ide_path_root = {'include_root' : '${project_root}/include',
                     'src_root'    : '${project_root}/src',
                     'test_root'   : '${project_root}/test'}

    @classmethod
    def create(cls, files, info):
        for key in files:
            cls.create_file(key, info)

    @classmethod
    def create_file(cls, key, info):
        target = cls.__get_target_file(key, info)
        template = cls.__get_template_file(key)
        cls.__do_create_file(template, target, info)

    @classmethod
    def __do_create_file(cls, src_file, target_file, info):
        template = Template(FileUtils.get_content(src_file))
        content = template.substitute(cls.__get_all_info(info))
        FileUtils.fullfill(target_file, content)

    @classmethod
    def __get_template_file(cls, key):
        cup_root = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(cup_root, 'template')
        return os.path.join(template_path, cls.template_files[key])

    @classmethod
    def __get_target_file(cls, key, info):
        return cls.__substitute(cls.target_files[key], info)

    @classmethod
    def __get_all_info(cls, info):
        result = {}
        for key, value in cls.ide_path_root.items():
            result[key] = cls.__substitute(value, info)
        return dict(result, **info)

    @classmethod
    def __substitute(cls, template_str, info):
        template = Template(template_str)
        return template.substitute(info)

