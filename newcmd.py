import os
from cupcfg import Cup
from projectgenerator import ProjectGenerator



class NewCmd:
    def __init__(self, args):
        if os.path.exists('.cup'):
            raise Exception('already exists cup project in this folder!')
        project = Cup.create(os.getcwd(), args.project_name)
        self.project_generator = ProjectGenerator(project, args.eclipse, args.build)

    def execute(self):
        self.project_generator.generate()


def run(args):
    cmd = NewCmd(args)
    cmd.execute()
    print('CUP: create project %s successful!' % args.project_name)