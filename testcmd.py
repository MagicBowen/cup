import os
from cupcfg import Cup
from projectbuilder import ProjectBuilder



class TestCmd:
    def __init__(self, args):
        project = Cup.load()
        self.builder = ProjectBuilder(project)
        self.test_paras = args.paras

    def execute(self):
        self.builder.build(test = True)
        self.builder.test(self.test_paras)


def run(args):
    cmd = TestCmd(args)
    cmd.execute()
    print('CUP: test project successful!')