import platform


class ProjectGenerator:
    base_files = ('project_cmake', 'namespace', 'src_cmake', 'test_cmake', 'test_main')
    eclipse_files = ('eclipse_project', 'eclipse_cproject')

    def __init__(self, project, with_eclipse, with_build):
        self.project = project
        self.eclipse = with_eclipse
        self.build = with_build

    def generate(self):
        files = self.__get_files_of_new_project()
        for file in files:
            self.project.create_file(file)

    def __get_files_of_new_project(self):
        files = []
        for file in self.base_files:
            files.append(file)
        if self.eclipse:
            for file in self.eclipse_files:
                files.append(file)
        if self.build:
            build_script = 'build_bat' if platform.system() == 'Windows' else 'build_sh'
            files.append(build_script)
        return files
