import os
from project import Project



class MoveCmd:
    def __init__(self, args):
        self.project = Project.load()
        self.source = args.source
        self.destination = args.destination

    def execute(self):
        pass


def run(args):
    cmd = MoveCmd(args)
    cmd.execute()
    print('CUP: move %s to %s successful!' % (args.src, args.dst))
