import os
import uuid


class Project:
    def __init__(self, name, root):
        self.name = name
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