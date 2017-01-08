import os
from string import Template
from ProjectInfo import ProjectInfo
from FileUtils import FileUtils

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
        ProjectInfo.init(project)

    def generate(self):
        self.__create_folder()
        self.__create_file()

    def __create_folder(self):
        for folder in self.folders:
            path = Template(folder).substitute(project = self.project)
            os.makedirs(os.path.join(os.getcwd(), os.path.join(self.project, path)))

    def __create_file(self):
        for item in self.files:
            path = Template(item[0]).substitute(project = self.project)
            target_file   = os.path.join(os.getcwd(), os.path.join(self.project, path))
            template_file = os.path.join(self.current_path, os.path.join('template', item[1]))
            self.__do_create_file(target_file, template_file)

    def __do_create_file(self, file, template_file):
        str = ProjectInfo.fill(FileUtils.get_content(template_file))
        FileUtils.set_content(file, str)


def new_project(args):
    if(os.path.exists(os.path.join(os.getcwd(), args.project))):
        print('CUP: %s is already exist, create failed!' % args.project)
        exit(1)

    ProjectGenerator(args.project).generate()
    print('CUP: create project %s successful!' % (args.project))
