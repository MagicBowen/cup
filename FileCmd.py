import os
import uuid
import configparser
from cupinfo import CupInfo
from project import Project



class FileGenerator:

    project = None

    @classmethod
    def generate(cls, args):
        cls.project = Project(cls.__get_project_name(), os.getcwd())
        if args.include:
            cls.__generate_file('header_file', args.file)
        elif args.src:
            cls.__generate_file('src_file', args.file)
        elif args.test:
            cls.__generate_file('test_file', args.file)
        elif args.struct:
            cls.__generate_file('header_file', args.file, postfix = 'h')
            cls.__generate_file('src_file', args.file, postfix = 'cpp')
        elif args.all:
            cls.__generate_file('header_file', args.file, postfix = 'h')
            cls.__generate_file('src_file', args.file, postfix = 'cpp')
            cls.__generate_file('test_file', args.file, prefix = 'Test', postfix = 'cpp')
        else:
            raise Exception('must specify the file type [-i | -s | -t | -c | -a]') 
        print('CUP: create file succesful!')

    @classmethod
    def __generate_file(cls, key, file, prefix = '', postfix = ''):
        file_path, file_name = os.path.split(file)
        struct_name = file_name.split('.')[0]
        include_path = os.path.join(cls.project.name, os.path.join(file_path, struct_name + '.h'))
        CupInfo.create_file(key, dict(cls.project.get_info(), 
                                      filepath = file_path, 
                                      filename = prefix + file_name + '.' + postfix,
                                      struct_header = include_path,
                                      struct = struct_name))

    @classmethod
    def __get_project_name(cls):
        config_file = cls.__get_config_file()
        cf = configparser.ConfigParser()
        cf.read(os.path.join(config_file))
        return  cf.get('project', 'name')  

    @classmethod
    def __get_config_file(cls):
        for dir in os.listdir(os.getcwd()):
            if '.cup' in dir:
                return dir
        raise Exception('not found project cup file, should in project root folder!')
