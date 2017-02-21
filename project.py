import os
import uuid
from fileutils import FileUtils



class Project:
    def __init__(self, cup, root, name, cfg):
        self.cup = cup
        self.cfg = cfg
        self.root = root
        self.name = name

    def create_file(self, file_type, path = None, **extra_info):
        self.cup.create_file(file_type, path, dict(self.__get_infos(), **extra_info))

    def get_relative_path(self, path):
        relative_path = FileUtils.get_rid_of_prefix_path(path, self.root)
        if relative_path.split(os.path.sep)[0] == 'include':
            relative_path = FileUtils.get_rid_of_top_path(relative_path)
        return FileUtils.get_rid_of_top_path(relative_path)  

    def get_name(self):
        return self.name

    def get_build_root(self):
        return os.path.join(self.root, 'build') 

    def get_build_make_type(self):
        return self.cfg.get('build', 'make')

    def get_build_macros(self):
        macros = self.cfg.get('build', 'macro')
        return [] if macros is None else macros.split(',')

    def get_build_target_type(self):
        return self.cfg.get('build', 'target')

    def get_test_name(self):
        return 'test_{}'.format(self.name)

    def get_root_of(self, key):
        return self.cup.get_project_file_root(key, self.root, self.name)

    def get_file_type(self, path):
        full_path = FileUtils.get_full_path(path)
        relative_path = FileUtils.get_rid_of_prefix_path(full_path, self.root)
        root = relative_path.split(os.path.sep)[0]
        if root == 'test': return 'test_file'
        elif root == 'include': return 'header_file'
        elif root == 'src': return 'src_file'
        else: return None

    def __get_infos(self):
        return { 'project_root'      : self.root
               , 'project_name'      : self.name
               , 'include_root'      : self.get_root_of('header_file')
               , 'src_root'          : self.get_root_of('src_file')
               , 'test_root'         : self.get_root_of('test_file')
               , 'namespace'         : self.__generate_namespace()
               , 'include_guard'     : self.__generate_include_guard()
               , 'test_include_path' : self.cfg.get('test', 'include')
               , 'test_link_path'    : self.cfg.get('test', 'link_path')
               , 'test_lib'          : self.cfg.get('test', 'lib')}

    def __generate_namespace(self):
        return self.name.upper() + '_NS'

    def __generate_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()    
