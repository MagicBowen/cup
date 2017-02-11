import os
from project import Project
from fileutils import FileUtils
from projectfile import ProjectFile



class NewCmd:
    def __init__(self, args):
        project = Project.load()
        self.files = []
        if args.include:
            self.files.append(ProjectFile(project, args.file, 'header_file'))
        elif args.src:
            self.files.append(ProjectFile(project, args.file, 'src_file'))
        elif args.test:
            self.files.append(ProjectFile(project, args.file, 'test_file'))
        elif args.struct:
            self.files.append(ProjectFile(project, args.file, 'header_file', postfix = '.h'))
            self.files.append(ProjectFile(project, args.file, 'src_file', postfix = '.cpp'))
        elif args.all:
            self.files.append(ProjectFile(project, args.file, 'header_file', postfix = '.h'))
            self.files.append(ProjectFile(project, args.file, 'src_file', postfix = '.cpp'))
            self.files.append(ProjectFile(project, args.file, 'test_file', prefix = 'Test', postfix = '.cpp'))
        else:
            self.files.append(ProjectFile(project, args.file))

    def execute(self):
        for file in self.files:
            file.generate()


def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)