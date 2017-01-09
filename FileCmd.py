import os
from CupInfo     import CupInfo
from ProjectInfo import ProjectInfo
from FileUtils   import FileUtils

class FileGenerator:
    templates = { 'include' : 'Struct.h.template'
                , 'src'     : 'Struct.cpp.template'
                , 'test'    : 'TestStruct.cpp.template'}

    @classmethod
    def generate(cls, args):
        files = {}
        if args.include:
            cls.__generate_file(args.file, 'include')
        elif args.src:
            cls.__generate_file(args.file, 'src')
        elif args.test:
            cls.__generate_file(args.file, 'test')
        elif args.struct:
            cls.__generate_file(args.file + '.h', 'include')
            cls.__generate_file(args.file + '.cpp', 'src')
        elif args.all:
            cls.__generate_file(args.file + '.h', 'include')
            cls.__generate_file(args.file + '.cpp', 'src')
            cls.__generate_file(args.file + '.cpp', 'test')
        else:
            raise Exception('must specify the file type [-i | -s | -t | -c | -a]')


    @classmethod
    def __generate_file(cls, file, type):
        template_file = os.path.join(CupInfo.template_path, cls.templates[type])
        file_path, file_name = os.path.split(file)
        struct_name = file_name.split('.')[0]
        full_path = os.path.join(ProjectInfo.paths[type], file_path)
        include_path = os.path.join(ProjectInfo.name, os.path.join(file_path, struct_name + '.h'))
        prefix = 'Test' if type == 'test' else ''
        target_file = os.path.join(full_path, prefix + file_name)

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        ProjectInfo.generate_file_by_template(template_file, target_file,
                                              struct_header = include_path,
                                              struct = struct_name)


def create_file(args):
    try:
        CupInfo.load()
        ProjectInfo.load()
        FileGenerator().generate(args)
        print('CUP: create file for %s successful!' % (args.file))
    except Exception as e:
        print('CUP: error occured,', e)
