import os
from fileutils import FileUtils



class ProjectFile:    
    def __init__(self, project, file, key = None, prefix = '', postfix = ''):
        self.project = project
        self.file = file
        self.key = key
        self.prefix = prefix
        self.postfix = postfix

    def generate(self):
        if self.key is None:
            FileUtils.create_file(os.path.join(os.getcwd(), self.file))
        else:
            self.project.generate_file( self.key
                                      , file_path = self.__get_file_path()
                                      , include_path = self.__get_include_path()
                                      , class_name = self.__get_class_name())

    def __get_file_path(self):
        path = self.__get_relative_path()
        filename = self.__get_file_name()
        return os.path.join(path, filename)

    def __get_include_path(self):
        header_name = self.__get_class_name() + '.h'
        header_path = self.__get_relative_path()
        return os.path.join(header_path, header_name)

    def __get_class_name(self):
        _, name = os.path.split(self.file)
        return name.split('.')[0]

    def __get_file_name(self):
        _, name = os.path.split(self.file)
        return self.prefix + name + self.postfix

    def __get_relative_path(self):
        path, _ = os.path.split(self.file)
        relative_path = self.project.get_relative_path(os.getcwd())
        return os.path.join(relative_path, path)    