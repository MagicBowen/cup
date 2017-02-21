import os
from templateutils import TemplateUtils
from fileutils import FileUtils
from projectcfg import ProjectConfig
from project import Project



class Cup:
    cup_templates =     { 'project_config'   : 'config.template'
                        , 'project_cmake'    : 'project.cmake.template'
                        , 'eclipse_project'  : 'eclipse.project.template'
                        , 'eclipse_cproject' : 'eclipse.cproject.template'
                        , 'build_sh'         : 'project.build.sh.template'
                        , 'build_bat'        : 'project.build.bat.template'                     
                        , 'namespace'        : 'project.h.template'
                        , 'src_cmake'        : 'src.cmake.template'
                        , 'test_cmake'       : 'test.cmake.template'
                        , 'test_main'        : 'test.main.cpp.template'
                        , 'header_file'      : 'header.template'
                        , 'src_file'         : 'src.template'
                        , 'test_file'        : 'test.template'
                        , 'user_file'        : 'user.template'}

    project_templates = { 'header_file'      : '${project_root}/.cup/templates/header.template'
                        , 'src_file'         : '${project_root}/.cup/templates/src.template'
                        , 'test_file'        : '${project_root}/.cup/templates/test.template'
                        , 'user_file'        : '${project_root}/.cup/templates/user.template'}                        
   
    target_files =      { 'project_config'   : '${project_root}/.cup/config'
                        , 'project_cmake'    : '${project_root}/CMakeLists.txt'
                        , 'eclipse_project'  : '${project_root}/.project'
                        , 'eclipse_cproject' : '${project_root}/.cproject'
                        , 'build_sh'         : '${project_root}/build.sh'
                        , 'build_bat'        : '${project_root}/build.bat' 
                        , 'namespace'        : '${project_root}/include/${project_name}/${project_name}.h'
                        , 'src_cmake'        : '${project_root}/src/CMakeLists.txt'
                        , 'test_cmake'       : '${project_root}/test/CMakeLists.txt'
                        , 'test_main'        : '${project_root}/test/main.cpp'}

    project_file_root = { 'header_file'      : '${project_root}/include/${project_name}'
                        , 'src_file'         : '${project_root}/src'
                        , 'test_file'        : '${project_root}/test'
                        , 'project_config'   : '${project_root}/.cup'}   

    @classmethod
    def create(cls, project_root, project_name):
        cls.__create_config(project_root, project_name)
        cls.__copy_templates(project_root, project_name)
        return Project(cls, project_root, project_name, ProjectConfig(cls.__get_config_file(project_root)))

    @classmethod
    def load(cls):
        project_root = cls.__find_project_root()
        if project_root is None : raise Exception('not found cup project')
        project_cfg = ProjectConfig(cls.__get_config_file(project_root))
        project_name = project_cfg.get('project', 'name')
        return Project(cls, project_root, project_name, project_cfg)

    @classmethod
    def create_file(cls, key, path, infos):
        template_path = cls.get_template_path(key, infos['project_root'])
        if path is None:
            target_path = cls.get_target_path(key, infos['project_root'], infos['project_name'])
        else:
            target_path = path
        content = TemplateUtils.replace(FileUtils.get_content(template_path), infos)
        FileUtils.create(target_path, content)  

    @classmethod
    def get_project_file_root(cls, key, project_root, project_name):
         return TemplateUtils.replace( cls.project_file_root[key]
                               , {'project_root' : project_root, 'project_name' : project_name})
         
    @classmethod
    def get_target_path(cls, key, project_root, project_name):
        return TemplateUtils.replace( cls.target_files[key]
                               , {'project_root' : project_root, 'project_name' : project_name})

    @classmethod
    def get_template_path(cls, key, project_root):
        if key in  cls.project_templates.keys():
            return  cls.__get_project_template_path(key, project_root)
        else:
            return cls.__get_cup_template_path(key)

    @classmethod
    def __get_cup_template_path(cls, key):
        cup_root = os.path.dirname(os.path.abspath(__file__))
        templates_path = os.path.join(cup_root, 'templates')
        return os.path.join(templates_path, cls.cup_templates[key])

    @classmethod
    def __get_project_template_path(cls, key, project_root):
        return TemplateUtils.replace(cls.project_templates[key], {'project_root' : project_root})

    @classmethod
    def __find_project_root(cls):
        path = os.getcwd()
        while path != '/':
            cup_path = os.path.join(path, '.cup')
            if os.path.exists(cup_path) and os.path.isdir(cup_path):
                return path
            path = os.path.dirname(path)
        return None

    @classmethod
    def __get_config_file(cls, project_root):
        return TemplateUtils.replace(cls.target_files['project_config'], {'project_root' : project_root})
        
    @classmethod
    def __create_config(cls, project_root, project_name):
        cls.create_file( 'project_config',   None, { 'project_root' : project_root
                                                   , 'project_name' : project_name})        

    @classmethod
    def __copy_templates(cls, project_root, project_name):
        for key in cls.project_templates.keys():
            cls.__copy_template(key, project_root)

    @classmethod
    def __copy_template(cls, key, project_root):
        target = cls.__get_project_template_path(key, project_root)
        source = cls.__get_cup_template_path(key)
        FileUtils.create(target, FileUtils.get_content(source))  

        