import os



class ProjectFile:    
    def __init__(self, project, file):
        self.project = project
        self.file = file

    def generate(self, key, prefix = '', postfix = ''):
        self.project.generate_file( key
                                  , file_path = self.__get_file_path(prefix, postfix)
                                  , include_path = self.__get_include_path()
                                  , class_name = self.__get_class_name())

    def __get_file_path(self, prefix, postfix):
        path = self.__get_relative_path()
        filename = self.__get_file_name(prefix, postfix)
        return os.path.join(path, filename)

    def __get_include_path(self):
        header_name = self.__get_class_name() + '.h'
        header_path = self.__get_relative_path()
        return os.path.join(header_path, header_name)

    def __get_class_name(self):
        _, name = os.path.split(self.file)
        return name.split('.')[0]

    def __get_file_name(self, prefix, postfix):
        _, name = os.path.split(self.file)
        return prefix + name + postfix

    def __get_relative_path(self):
        path, _ = os.path.split(self.file)
        relative_path = self.project.get_relative_path(os.getcwd())
        return os.path.join(relative_path, path)    