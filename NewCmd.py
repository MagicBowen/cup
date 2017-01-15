import os
import platform
from project import Project
from cupinfo import CupInfo


class ProjectGenerator:
    base_files = ['project_config', 'project_cmake', 'namespace', 'src_cmake', 'test_cmake', 'test_main']
    eclipse_files = ['eclipse_project', 'eclipse_cproject']

    @classmethod
    def generate(cls, args):
        project_name = args.project
        project_root = os.path.join(os.getcwd(), project_name)

        if os.path.exists(project_root):
            print('CUP: %s is already exist, create failed!' % project_name)
            exit(1)

        build_bash = 'build_bat' if platform.system() == 'Windows' else 'build_sh'
        cls.base_files.append(build_bash)

        project = Project(project_name, project_root)
        CupInfo.create(cls.base_files, project.get_info())
        if args.ide:
            CupInfo.create(cls.eclipse_files, project.get_info())

        print('CUP: create project %s successful!' % project_name)
