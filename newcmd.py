import os
from project import Project
from fileutils import FileUtils



class NewCmd:
    def __init__(self, args):
        self.project = Project.load()
        self.file = args.file
        self.args = args

    def execute(self):
        if self.args.include:
            self.__generate_file('header_file', self.file)
        elif self.args.src:
            self.__generate_file('src_file', self.file)
        elif self.args.test:
            self.__generate_file('test_file', self.file)
        elif self.args.struct:
            self.__generate_file('header_file', self.file, postfix = '.h')
            self.__generate_file('src_file', self.file, postfix = '.cpp')
        elif self.args.all:
            self.__generate_file('header_file', self.file, postfix = '.h')
            self.__generate_file('src_file', self.file, postfix = '.cpp')
            self.__generate_file('test_file', self.file, prefix = 'Test', postfix = '.cpp')
        else:
            raise Exception('must specify the file type [-i | -s | -t | -c | -a]') 

    def __generate_file(self, key, file, prefix = '', postfix = ''):
        self.project.generate_file( key
                                  , file_path = self.__get_file_path(file, prefix, postfix)
                                  , include_path = self.__get_include_path(file)
                                  , struct = self.__get_struct_name(file))

    def __get_file_path(self, file, prefix, postfix):
        path = self.__get_path(file)
        filename = self.__get_file_name(file, prefix, postfix)
        return os.path.join(path, filename)

    def __get_include_path(self, file):
        header_name = self.__get_struct_name(file) + '.h'
        header_path = self.__get_path(file)
        return os.path.join(header_path, header_name)

    def __get_struct_name(self, file):
        _, name = os.path.split(file)
        return name.split('.')[0]

    def __get_file_name(self, file, prefix, postfix):
        _, name = os.path.split(file)
        return prefix + name + postfix

    def __get_path(self, file):
        path, _ = os.path.split(file)
        relative_path = self.project.get_relative_path(os.getcwd())
        return os.path.join(relative_path, path)



def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)