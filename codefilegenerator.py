import os
from fileutils import FileUtils



class CodeFileGenerator:

    fixes = { 'user_file'   : (''    , '')
            , 'header_file' : (''    , '.h')
            , 'src_file'    : (''    , '.cpp')
            , 'test_file'   : ('Test', '.cpp')}

    def __init__(self, project, file_path, file_type):
        self.project = project
        self.type = file_type
        self.file_path = self.__get_full_path(file_path)
        print(self.file_path)

    def generate(self):
        self.project.create_file( self.type
                                , self.file_path
                                , include_path = self.__get_include_path()
                                , class_name = self.__get_class_name())

    def __get_full_path(self, file_path):
        path = self.__get_path(file_path)
        name = self.__get_name(file_path)
        return os.path.join(path, name)

    def __get_include_path(self):
        header_name = self.__get_class_name() + '.h'
        header_path = self.__get_relative_path()
        return os.path.join(header_path, header_name)        

    def __get_class_name(self):
        file_base = FileUtils.get_base_name(self.file_path)
        return self.__strip_prefix(file_base)

    def __strip_prefix(self, file_base):
        prefix = self.__get_prefix()
        prefix_len = len(prefix)
        return file_base[prefix_len:] if file_base[0 : prefix_len] == prefix else file_base      

    def __get_relative_path(self):
        relative_path = self.project.get_relative_path(self.file_path)
        return os.path.split(relative_path)[0] 

    def __get_path(self, file_path):
        full_path = os.path.join(os.getcwd(), FileUtils.get_path(file_path))
        if self.type == 'user_file': return full_path
        relative_path = self.project.get_relative_path(full_path)
        project_path = self.project.get_root_of(self.type)
        return os.path.join(project_path, relative_path)

    def __get_name(self, file_path):
        name = FileUtils.get_name(file_path)
        return self.__generate_name(name)

    def __generate_name(self, name):
        if FileUtils.get_postfix(name) is None:
            name = name + self.__get_postfix()
        if not FileUtils.start_from(name, self.__get_prefix()):
            name = self.__get_prefix() + name
        return name

    def __get_prefix(self):
        return self.fixes[self.type][0]

    def __get_postfix(self):
        return self.fixes[self.type][1]
