import os
import uuid
from projectconfig import ProjectConfig
from cupinfo import CupInfo
from fileutils import FileUtils



class Project:
    @classmethod
    def new(cls, root, name):
        cfg = ProjectConfig(root)
        cfg.save_default(name)
        return cls.load()

    @classmethod
    def load(cls):
        cfg = ProjectConfig()
        return cls(cfg.load())

    def __init__(self, cfg):
        self.cfg = cfg
        self.name = cfg['project']['name']
        self.root = cfg['root']

    def generate(self):
        files = self.__get_default_files()
        for file in files:
            self.generate_file(file)

    def generate_file(self, file, **paras):
        CupInfo.create_file(file, dict(self.__get_info(), **paras))

    def get_relative_path(self, path):
        relative_path = FileUtils.get_rid_of_prefix_path(path, self.root)
        if relative_path.split(os.path.sep)[0] == 'include':
            relative_path = FileUtils.get_rid_of_top_path(relative_path)
        return FileUtils.get_rid_of_top_path(relative_path)   

    def get_include_root(self):
        return os.path.join(os.path.join(self.root, 'include'), self.name)

    def get_src_root(self):
        return os.path.join(self.root, 'src')

    def get_test_root(self):
        return os.path.join(self.root, 'test')

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
               , 'test_lib'          : self.cfg['test']['lib']}

    def __generate_namespace(self):
        return self.name.upper() + '_NS'

    def __generate_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()
