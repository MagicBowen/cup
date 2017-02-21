from cupcfg import Cup
from projectbuilder import ProjectBuilder



class BuildCmd:
    def __init__(self, args):
        project = Cup.load()
        self.builder = ProjectBuilder(project)
        self.is_clean = args.clean

    def execute(self):
        if not self.is_clean:
            self.builder.build()
            print('CUP: build project successful!')
        else:
            self.builder.clean()
            print('CUP: clean project successful!')


def run(args):
    cmd = BuildCmd(args)
    cmd.execute()
        