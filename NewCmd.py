import os
from project import Project



class NewCmd:
    def __init__(self, args):
        self.project = Project.load(os.getcwd())
        self.args = args

    def execute(self):
        if self.args.include:
            self.__generate_file('header_file', self.args.file)
        elif self.args.src:
            self.__generate_file('src_file', self.args.file)
        elif self.args.test:
            self.__generate_file('test_file', self.args.file)
        elif self.args.struct:
            self.__generate_file('header_file', self.args.file, postfix = '.h')
            self.__generate_file('src_file', self.args.file, postfix = '.cpp')
        elif self.args.all:
            self.__generate_file('header_file', self.args.file, postfix = '.h')
            self.__generate_file('src_file', self.args.file, postfix = '.cpp')
            self.__generate_file('test_file', self.args.file, prefix = 'Test', postfix = '.cpp')
        else:
            raise Exception('must specify the file type [-i | -s | -t | -c | -a]') 

    def __generate_file(self, key, file, prefix = '', postfix = ''):
        path, name = os.path.split(file)
        if path != '' : path = '/' + path
        struct = name.split('.')[0]
        filename = prefix + name + postfix
        self.project.generate_file(key, filepath = path, filename = filename, struct = struct)


def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)