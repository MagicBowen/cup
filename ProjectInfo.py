import os
import uuid
import configparser 
from string import Template
from FileUtils import FileUtils


class ProjectInfo:
    name = None
    namespace = None
    root_path = None
    include_path = None
    src_path = None
    test_path = None
    config_path = None

    @classmethod
    def init(cls, project):
        cls.name = project
        cls.namespace = cls.name.upper() + '_NS'
        cls.init_path()

    @classmethod
    def init_path(cls):
        cls.root_path = os.getcwd()
        project_name = os.path.split(cls.root_path)[-1] if cls.name is None else cls.name
        cls.include_path = os.path.join(os.path.join(cls.root_path, 'include'), project_name)
        cls.src_path = os.path.join(cls.root_path, 'src')
        cls.test_path = os.path.join(cls.root_path, 'test')
        cls.config_path = os.path.join(cls.root_path, 'cup')

    @classmethod
    def load(cls):
        cls.init_path()
        files = FileUtils.search_file_by_postfix(cls.config_path, '.cup')
        if len(files) != 1:
            raise Exception('not exist project cup file')
        cls.load_config(files[0])

    @classmethod
    def load_config(cls, config_file):
        cf = configparser.ConfigParser()
        cf.read(os.path.join(cls.config_path, config_file))
        project_name = cf.get('project', 'name')
        cls.init(project_name)

    @classmethod
    def fill(cls, template_str, dict): 
        target_dict = dict.copy()
        target_dict['project'] = cls.name
        target_dict['namespace'] = cls.namespace
        target_dict['include_guard'] = cls.generate_include_guard()

        template = Template(template_str)
        result = template.substitute(target_dict)   
        return result

    @classmethod
    def generate_file_by_template(cls, template, target, **target_dict):
        str = cls.fill(FileUtils.get_content(template), target_dict)
        FileUtils.set_content(target, str)  

    @classmethod
    def generate_include_guard(cls):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()