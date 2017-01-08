import uuid
from string import Template


class ProjectInfo:
    name = None
    namespace = None

    @classmethod
    def init(cls, project):
        cls.name = project
        cls.namespace = cls.name.upper() + '_NS'

    @classmethod
    def isCreated(cls):
        return cls.name is None

    @classmethod
    def fill(cls, template_str): 
        template = Template(template_str)
        result = template.substitute( project = cls.name
                                    , namespace = cls.namespace
                                    , include_guard = cls.generate_include_guard())   
        return result    

    @classmethod
    def generate_include_guard(cls):
        uuid_str = str(uuid.uuid1())
        return 'H' + uuid_str.replace('-', '_').upper()