import os
from string import Template
from ProjectInfo import ProjectInfo
from FileUtils import FileUtils
from CupInfo   import CupInfo

class ProjectGenerator(object):
    files = [('CMakeLists.txt'                     , 'project.cmake.template'),
             ('include/$project/$project.h'        , 'project.h.template'),
             ('src/CMakeLists.txt'                 , 'src.cmake.template'),
             ('test/CMakeLists.txt'                , 'test.cmake.template'),
             ('test/main.cpp'                      , 'test.main.cpp.template'),
             ('cup/build.sh'                       , 'project.build.sh.template'),
             ('cup/build.bat'                      , 'project.build.bat.template'),
             ('cup/$project.cup'                   , 'project.cup.template')]    

    sample = [('include/$project/Sample.h'         , 'Sample.h.template'),
              ('src/Sample.cpp'                    , 'Sample.cpp.template'),
              ('test/TestSample.cpp'               , 'TestSample.cpp.template')]

    ide    = [('cup/project/.project'              , 'eclipse.project.template'),
              ('cup/project/.cproject'             , 'eclipse.cproject.template')]

    def __init__(self, project):
        self.project = project
        ProjectInfo.init(project)

    def generate(self, with_sample, with_ide):
        self.__create_folders()
        self.__create_files(self.files)
        if with_sample:
            self.__create_files(self.sample)
        if with_ide:
            self.__create_files(self.ide)

    def __create_folders(self):
        for folder in ProjectInfo.folders:
            path = Template(folder).substitute(project = self.project)
            os.makedirs(os.path.join(os.getcwd(), os.path.join(self.project, path)))

    def __create_files(self , files):
        for item in files:
            path = Template(item[0]).substitute(project = self.project)
            target_file   = os.path.join(os.getcwd(), os.path.join(self.project, path))
            template_file = os.path.join(CupInfo.template_path, item[1])
            ProjectInfo.generate_file_by_template(template_file, target_file)


def new_project(args):
    if(os.path.exists(os.path.join(os.getcwd(), args.project))):
        print('CUP: %s is already exist, create failed!' % args.project)
        exit(1)

    CupInfo.load()
    ProjectGenerator(args.project).generate(args.sample, args.ide)
    print('CUP: create project %s successful!' % (args.project))
