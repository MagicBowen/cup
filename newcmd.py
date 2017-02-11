import os
from project import Project
from fileutils import FileUtils
from projectfile import ProjectFile



class NewCmd:
    def __init__(self, args):
        self.project = Project.load()
        self.file = ProjectFile(self.project, args.file)
        self.args = args

    def execute(self):
        if self.args.include:
            self.file.generate('header_file')
        elif self.args.src:
            self.file.generate('src_file')
        elif self.args.test:
            self.file.generate('test_file')
        elif self.args.struct:
            self.file.generate('header_file', postfix = '.h')
            self.file.generate('src_file', postfix = '.cpp')
        elif self.args.all:
            self.file.generate('header_file', postfix = '.h')
            self.file.generate('src_file', postfix = '.cpp')
            self.file.generate('test_file', prefix = 'Test', postfix = '.cpp')
        else:
            self.__generate_default_file(self.args.file)

    def __generate_default_file(self, file):
        FileUtils.create_file(os.path.join(os.getcwd(), file))


def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)