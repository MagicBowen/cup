import os
from CupInfo     import CupInfo
from ProjectInfo import ProjectInfo
from FileUtils   import FileUtils

class FileGenerator:
    templates = { 'header' : 'Struct.h.template'
                , 'source' : 'Struct.cpp.template'
                , 'test'   : 'TestStruct.cpp.template'}

    @classmethod
    def generate_file(cls, file, type, project_path):
        template_file = os.path.join(CupInfo.template_path, cls.templates[type])
        file_path, file_name = os.path.split(file)
        struct_name = file_name.split('.')[0]
        full_path = os.path.join(project_path, file_path)
        include_path = os.path.join(ProjectInfo.name, os.path.join(file_path, struct_name + '.h'))
        target_file = os.path.join(full_path, file_name)

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        ProjectInfo.generate_file_by_template(template_file, target_file,
                                              struct_header = include_path,
                                              struct = struct_name)

    @classmethod
    def generate(cls, args):
        files = {}
        if args.header:
            cls.generate_file(args.file, 'header', ProjectInfo.include_path)
        if args.source:
            cls.generate_file(args.file, 'source', ProjectInfo.src_path)
        if args.test:
            cls.generate_file(args.file, 'test', ProjectInfo.test_path)
        if args.struct:
            cls.generate_file(args.file + '.h', 'header', ProjectInfo.include_path)
            cls.generate_file(args.file + '.cpp', 'source', ProjectInfo.src_path)
        if args.all:
            cls.generate_file(args.file + '.h', 'header', ProjectInfo.include_path)
            cls.generate_file(args.file + '.cpp', 'source', ProjectInfo.src_path)
            cls.generate_file(args.file + '.cpp', 'test', ProjectInfo.test_path)
            


def create_file(args):
        CupInfo.load()
        ProjectInfo.load()
        FileGenerator().generate(args)

        print('CUP: create file for %s successful!' % (args.file))
