import os
from project import Project
from fileutils import FileUtils



class NewCmd:
    def __init__(self, args):
        self.project = Project.load()
        self.args = args

    def execute(self):
        file_path = self.__get_relative_path_to_project(self.args.file)
        if self.args.include:
            self.__generate_file('header_file', file_path)
        elif self.args.src:
            self.__generate_file('src_file', file_path)
        elif self.args.test:
            self.__generate_file('test_file', file_path)
        elif self.args.struct:
            self.__generate_file('header_file', file_path, postfix = '.h')
            self.__generate_file('src_file', file_path, postfix = '.cpp')
        elif self.args.all:
            self.__generate_file('header_file', file_path, postfix = '.h')
            self.__generate_file('src_file', file_path, postfix = '.cpp')
            self.__generate_file('test_file', file_path, prefix = 'Test', postfix = '.cpp')
        else:
            raise Exception('must specify the file type [-i | -s | -t | -c | -a]') 

    def __generate_file(self, key, file, prefix = '', postfix = ''):
        path, name = os.path.split(file)
        if path != '' : path = '/' + path
        struct = name.split('.')[0]
        filename = prefix + name + postfix
        self.project.generate_file(key, filepath = path, filename = filename, struct = struct)

    def __get_relative_path_to_project(self, file):
        project_root = self.project.get_info()['project_root']
        relative = FileUtils.get_rid_of_prefix_path(os.getcwd(), project_root)
        if relative.split(os.path.sep)[0] == 'include':
            relative = FileUtils.get_rid_of_top_path(relative)
        return os.path.join(FileUtils.get_rid_of_top_path(relative), file)



def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)