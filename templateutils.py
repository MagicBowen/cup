from string import Template


class TemplateUtils:
    @classmethod
    def replace(cls, template_str, infos):
        template = Template(template_str)
        return template.substitute(infos)    
