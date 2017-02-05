import os
from project import Project



class MoveCmd:
    def __init__(self, args):
        self.project = Project.load(os.getcwd())
        self.args = args

    def execute(self):
        pass


def run(args):
    cmd = MoveCmd(args)
    cmd.execute()
    print('CUP: move %s to %s successful!' % (args.src, args.dst))
