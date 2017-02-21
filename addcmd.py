import os
from cupcfg import Cup
from fileutils import FileUtils
from codefilegenerator import CodeFileGenerator


class AddCmd:
    def __init__(self, args):
        self.project = Cup.load()
        self.file = args.file
        self.__verify_para(args)
        self.__init_files(args)

    def execute(self):
        for file in self.files:
            file.generate()

    def __verify_para(self, args):
        if args.struct or args.all:
            if FileUtils.get_postfix(args.file) is not None:
                raise Exception('can not generate class with postfix')
            if self.project.get_file_type(args.file) == 'test_file':
                raise Exception('can not generate class in test folder')            

    def __init_files(self, args):
        self.files = []
        if args.include:
            self.__append_files('header_file')
        elif args.src:
            self.__append_files('src_file')
        elif args.test:
            self.__append_files('test_file')
        elif args.struct:
            self.__append_files('header_file', 'src_file')
        elif args.all:
            self.__append_files('header_file', 'src_file', 'test_file')
        else:
            self.__append_files('user_file')

    def __append_files(self, *file_types):
        for file_type in file_types:
            self.files.append(CodeFileGenerator(self.project, self.file, file_type))



def run(args):
    cmd = AddCmd(args)
    cmd.execute()
    print('CUP: create %s successful!' % args.file)