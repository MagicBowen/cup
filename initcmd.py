import os
from project import Project



class InitCmd:
    def __init__(self, args):
        try:
            self.project = Project.new(os.getcwd(), args.project)
        except Exception as e:
            print("CUP failed: %s" % (e))

    def execute(self):
        pass


def run(args):
    cmd = InitCmd(args)
    cmd.execute()