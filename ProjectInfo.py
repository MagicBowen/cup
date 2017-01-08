import os
import uuid
import configparser 
from string import Template
from FileUtils import FileUtils


class ProjectInfo:
    folders = ['include/$project', 'src', 'test', 'cup']
    name = None
    namespace = None
    root_path = None
    paths = {}

    @classmethod
    def init(cls, project):
        cls.name = project
        cls.namespace = cls.name.upper() + '_NS'

    @classmethod
    def load_path(cls):
        cls.root_path = os.path.dirname(os.getcwd())
        project_name = os.path.split(cls.root_path)[-1] if cls.name is None else cls.name
        cls.paths['include'] = os.path.join(os.path.join(cls.root_path, 'include'), project_name)
        cls.paths['src'] = os.path.join(cls.root_path, 'src')
        cls.paths['test'] = os.path.join(cls.root_path, 'test')
        cls.paths['cfg']  = os.path.join(cls.root_path, 'cup')

    @classmethod
    def load(cls):
        if not cls.cwd_ok():
            raise Exception('not in the project cup folder')
        cls.load_path()
        cls.load_config(cls.get_cfg_file())

    @classmethod
    def cwd_ok(cls):
        files = FileUtils.search_file_by_postfix(os.getcwd(), '.cup')
        return True if len(files) == 1 else False

    @classmethod
    def get_cfg_file(cls):
        files = FileUtils.search_file_by_postfix(cls.paths['cfg'], '.cup')
        if len(files) != 1:
            raise Exception('not found the correct cup config file') 
        return files[0]    

    @classmethod
    def load_config(cls, config_file):
        cf = configparser.ConfigParser()
        cf.read(os.path.join(cls.paths['cfg'], config_file))
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