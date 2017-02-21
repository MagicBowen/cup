import os
import shutil
from systemutils import SystemUtils



class ProjectBuilder:
    def __init__(self, project):
        self.project = project

    def build(self, test = False):
        current_folder = os.getcwd()
        try:
            self.__chdir_to_build()
            self.__generate_makefile(test)
            self.__make_project()

        except Exception as e:
            print('build project failed!')
            raise e

        finally:
            os.chdir(current_folder)

    def test(self, paras):
        try:
            self.__run_test(paras)

        except Exception as e:
            print('test project failed!')
            raise e    

    def clean(self):
        build_folder = self.project.get_build_root()
        shutil.rmtree(build_folder)

    def __chdir_to_build(self):
        build_folder = self.project.get_build_root()
        if not os.path.exists(build_folder):
            os.mkdir(build_folder)
        os.chdir(build_folder)   

    def __generate_makefile(self, test):
        self.__print_split_line()
        print("start to build %s ..." % self.project.get_name())
        SystemUtils.exec('cmake %s ..' % self.__generate_cmake_para(test)) 

    def __generate_cmake_para(self, test):
        make_type_paras = self.__get_make_type_paras()
        macro_paras = self.__get_macro_paras(test)
        return '{} {}'.format(make_type_paras, macro_paras)

    def __get_make_type_paras(self):
        make_type = self.project.get_build_make_type()
        return '' if make_type is None else "-G '{}'".format(make_type)

    def __get_macro_paras(self, test):
        macro_para = '' if not test else self.__get_macro_para('ENABLE_TEST=1')
        for macro in self.project.get_build_macros():
            macro_para += self.__get_macro_para(macro)   
        return macro_para     

    def __get_macro_para(self, para):
        return '-D{}'.format(para)

    def __make_project(self):
        SystemUtils.exec('cmake --build . %s' % self.__generate_build_config_para())

    def __generate_build_config_para(self):
        target = self.project.get_build_target_type()
        return '' if target is None else '--config {}'.format(target)

    def __run_test(self, paras):
        test = self.__find_executable_test()
        if test is None : raise Exception('have not found executable test')
        SystemUtils.exec('{} {}'.format(test, paras))

    def __find_executable_test(self):
        test_name = self.project.get_test_name()
        build_folder = os.path.join(self.project.get_build_root(), 'test')
        return SystemUtils.find_file_by_name(build_folder, test_name)

    def __print_split_line(self):
        print('-' * 80)

