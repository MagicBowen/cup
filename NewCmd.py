import os
import uuid
from string import Template


class ProjectGenerator(object):
    folders = ['include/$project', 'src', 'test', 'cup']

    files = [('CMakeLists.txt'                     , 'project.cmake.template'),
             ('include/$project/$project.h'        , 'project.h.template'),
             ('include/$project/CupExample.h'      , 'CupExample.h.template'),
             ('src/CupExample.cpp'                 , 'CupExample.cpp.template'),
             ('src/CMakeLists.txt'                 , 'src.cmake.template'),
             ('test/CMakeLists.txt'                , 'test.cmake.template'),
             ('test/main.cpp'                      , 'test.main.cpp.template'),
             ('test/TestCupExample.cpp'            , 'TestCupExample.cpp.template'),
             ('cup/build.sh'                       , 'project.build.sh.template'),
             ('cup/build.bat'                      , 'project.build.bat.template'),
             ('cup/$project.cup'                   , 'project.cup.template')]    

    def __init__(self, project):
        self.project = project
        self.current_path = os.path.dirname(os.path.abspath(__file__))

    def generate(self):
        self.__create_folder()
        self.__create_file()

    def __create_folder(self):
        for folder in ProjectGenerator.folders:
            path = Template(folder).substitute(project = self.project)
            os.makedirs(os.path.join(os.getcwd(), os.path.join(self.project, path)))

    def __create_file(self):
        for item in ProjectGenerator.files:
            path = Template(item[0]).substitute(project = self.project)
            target_file   = os.path.join(os.getcwd(), os.path.join(self.project, path))
            template_file = os.path.join(self.current_path, os.path.join('template', item[1]))
            self.__do_create_file(target_file, template_file)

    def __do_create_file(self, file, template_file):
        template = Template(self.__get_template_str(template_file))
        str=template.substitute( project = self.project
                               , project_upper = self.project.upper()
                               , include_guard = self.__get_include_guard())
        with open(file, 'w') as f: f.write(str)
            
    def __get_template_str(self, template):
        with open(template, 'r') as f:
            return f.read()

    def __get_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()


def new_project(args):
    ProjectGenerator(args.project).generate()
    print('CUP: create project %s successful!' % (args.project))
