import os
from project import Project



class UpdateCmd:
    def __init__(self, args):
        self.project = Project.load()

    def execute(self):
        pass

def run(args):
    cmd = UpdateCmd(args)
    cmd.execute()
    print('CUP: update project un-supported now!')