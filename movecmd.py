import os
from project import Project
from fileutils import FileUtils



class MoveCmd:
    def __init__(self, args):
        self.project = Project.load()
        self.source = args.source
        self.destination = args.destination

    def execute(self):
        self.__verify_src_dst()
        source_file = self.__get_full_include_path(self.source)
        target_file = self.__get_full_include_path(self.destination)

        # self.__move_header()
        # self.__move_src()
        # self.__move_test()

    def __get_source_class_name(self):
        pass

    def __verify_src_dst(self):
        if not self.__is_exist(self.source): 
            raise Exception('source %s is not existed' % (self.source))
        if self.__is_exist(self.destination):
            raise Exception('destination %s is existed' % (self.destination))

    def __is_exist(self, path):
        full_path = self.__get_full_include_path(path)
        return os.path.exists(full_path)

    def __get_full_include_path(self, path):
        return os.path.join(self.project.get_include_root(), path)


def run(args):
    cmd = MoveCmd(args)
    cmd.execute()
    print('CUP: move %s to %s successful!' % (args.src, args.dst))
