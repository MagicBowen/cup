import os
import uuid
import ConfigParser
from string import Template


class NewCmd(object):
    folders = ['include/$project', 'src', 'test', 'deps', 'project', 'doc']

    files = [('CMakeLists.txt'              , 'project.cmake.template'),
             ('include/$project/$project.h' , 'project.h.template'),
             ('src/CMakeLists.txt'          , 'src.cmake.template'),
             ('src/$project.cpp'            , 'src.cpp.template'),
             ('test/CMakeLists.txt'         , 'test.cmake.template'),
             ('test/main.cpp'               , 'test.main.cpp.template'),
             ('test/testcase.cpp'           , 'test.testcase.cpp.template'),
             ('project/build.sh'            , 'project.build.sh.template'),
             ('project/build.bat'           , 'project.build.bat.template'),
             ('project/cup.toml'            , 'cup.toml.template')]    

    def __init__(self, project):
        self.project = project
        self.current_path = os.path.dirname(os.path.abspath(__file__))

    def execute(self):
        self.__create_folder()
        self.__create_file()

    def __create_folder(self):
        for folder in NewCmd.folders:
            path = Template(folder).substitute(project = self.project)
            os.makedirs(os.path.join(os.getcwd(), os.path.join(self.project, path)))

    def __create_file(self):
        for item in NewCmd.files:
            path = Template(item[0]).substitute(project = self.project)
            target_file   = os.path.join(os.getcwd(), os.path.join(self.project, path))
            template_file = os.path.join(self.current_path, os.path.join('template', item[1]))
            self.__do_create_file(target_file, template_file)

    def __do_create_file(self, file, template_file):
        print(file)
        print(template_file)
        config = ConfigParser.ConfigParser()
        config.readfp(open(os.path.join(self.current_path, 'config/test.ini')))
        template = Template(self.__get_template_str(template_file))
        str=template.substitute( project = self.project
                               , project_upper = self.project.upper()
                               , include_guard = self.__get_include_guard()
                               , test_include = config.get("Default", "include_path")
                               , test_lib_dir = config.get("Default", "link_path")
                               , test_lib = config.get("Default", "lib_name"))
        with open(file, 'w') as f: f.write(str)
            
    def __get_template_str(self, template):
        with open(template, 'r') as f:
            return f.read()

    def __get_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()

def new_cmd(args):
    cmd = NewCmd(args.project)
    cmd.execute()
