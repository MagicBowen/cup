import os
import json
import uuid



class Project:
    @classmethod
    def new(cls, root, name):
        cls.__create_config_file(root, name)
        return cls.load(root, name)

    @classmethod
    def load(cls, root, name):
        with open(cls.__get_cfg_file_name(root, name), 'r') as f:
            cfg = json.load(f)
            return cls(cfg, root)

    @classmethod
    def __create_config_file(cls, root, name):
        cfg_file = cls.__get_cfg_file_name(root, name)
        if os.path.exists(cfg_file):
            raise Exception('project %s already exists' % (name))
        with open(cfg_file, 'w') as f:
            json.dump(cls.__get_default_config(name), f, indent=4)

    @classmethod
    def __get_cfg_file_name(cls, root, name):
        filename = '{}.cup'.format(name)
        return os.path.join(root, filename)

    @classmethod
    def __get_default_config(cls, name):
        return  { 'name' : name
                , 'project_type' : 'eclipse'
                , 'test' : {'include' : ['ENV{GTEST_PATH}/include'], 
                            'link_path' : ['ENV{GTEST_PATH}/lib'], 
                            'lib' : ['gtest.a'],
                            'exclude' : None}
                }

    def __init__(self, cfg, root):
        self.cfg = cfg
        self.name = cfg['name']
        self.root = root

    def get_info(self):
        return {'project'       : self.name,
                'project_root'  : self.root,
                'namespace'     : self.__generate_namespace(),
                'include_guard' : self.__generate_include_guard()}

    def __generate_namespace(self):
        return self.name.upper() + '_NS'

    def __generate_include_guard(self):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()