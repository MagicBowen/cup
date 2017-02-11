import os
import platform
import configparser



class ProjectConfig:
    def __init__(self, root = None):
        self.root = self.__get_root() if root is None else root
        self.parser = configparser.ConfigParser()

    def save_default(self, project_name):
        self.parser.add_section('project')
        self.parser.set('project', 'name', project_name)
        self.parser.set('project', 'ide', 'eclipse')

        self.parser.add_section('build')
        self.parser.set('build', 'os', platform.system())
        self.parser.set('build', 'bit', platform.architecture()[0])
        self.parser.set('build', 'target', 'Debug')

        self.parser.add_section('test')
        self.parser.set('test', 'include', '$ENV{GTEST_HOME}/include')
        self.parser.set('test', 'link_path', '$ENV{GTEST_HOME}/lib')
        self.parser.set('test', 'lib', 'gtest')
        self.parser.set('test', 'exclude', 'None')

        self.parser.add_section('depends')

        self.parser.write(open(self.__get_path(project_name), "w"))

    def load(self):
        self.parser.read(self.__get_config_file())
        cfg = {'root' : self.root}
        for section in self.parser.sections():
            subcfg = {}
            for item in self.parser.items(section):
                subcfg[item[0]] = item[1]
            cfg[section] = subcfg
        return cfg

    def __get_root(self):
        path = os.getcwd()
        while path != '/':
            project_cfg = self.__find_anchor(path)
            if project_cfg is not None:
                return path
            path = os.path.dirname(path)
        raise Exception('not found project cup file!')

    def __find_anchor(self, path):
        for dir in os.listdir(path):
            if '.cup' in dir:
                return dir
        return None

    def __get_config_file(self):
        file = self.__find_anchor(self.root)
        if file is not None : return os.path.join(self.root, file)
        raise Exception('not found project cup file, should in project root folder!')        

    def __get_path(self, project_name):
        return os.path.join(self.root, '{}.cup'.format(project_name))

