import os
from project import Project



class InitCmd:
    def __init__(self, args):
        self.project = Project.new(os.getcwd(), args.project)

    def execute(self):
        self.project.generate()


def run(args):
    cmd = InitCmd(args)
    cmd.execute()
    print('CUP: create project %s successful!' % args.project)