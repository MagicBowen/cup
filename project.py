import os
import uuid
from projectconfig import ProjectConfig
from cupinfo import CupInfo



class Project:
    @classmethod
    def new(cls, root, name):
        cfg = ProjectConfig(root)
        cfg.save_default(name)
        return cls.load(root)

    @classmethod
    def load(cls, root):
        cfg = ProjectConfig(root)
        return cls(cfg.load(), root)

    def __init__(self, cfg, root):
        self.cfg = cfg
        self.name = cfg['project']['name']
        self.root = root

    def generate(self):
        files = self.__get_default_files()
        for file in files:
            self.generate_file(file)

    def generate_file(self, file, **paras):
        CupInfo.create_file(file, dict(self.__get_info(), **paras))

    def __get_default_files(self):
        return  [ 'project_cmake'
                , 'namespace'
                , 'src_cmake'
                , 'test_cmake'
                , 'test_main'
                , 'eclipse_project'
                , 'eclipse_cproject'
                , 'build_bat' if self.cfg['build']['os'] == 'Windows' else 'build_sh']

    def __get_info(self):
        return { 'project'           : self.name
               , 'project_root'      : self.root
               , 'namespace'         : self.__generate_namespace()
               , 'include_guard'     : self.__generate_include_guard()
               , 'test_include_path' : self.cfg['test']['include']
               , 'test_link_path'    : self.cfg['test']['link_path']
               , 'test_lib'          : self.cfg['test']['lib']
               , 'include_root'      : '{}/include'.format(self.root)
               , 'src_root'          : '{}/src'.format(self.root)
               , 'test_root'         : '{}/test'.format(self.root)}

    def __generate_namespace(self):
        return self.name.upper() + '_NS'

    def __generate_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()
