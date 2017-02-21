import os


class FileUtils:
    @classmethod
    def get_content(cls, file):
        with open(file, 'r') as f:
            return f.read()

    @classmethod
    def create(cls, file, content = ''):
        path, _ = os.path.split(file)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(file, 'w') as f: f.write(content)

    @classmethod
    def get_full_path(cls, relative_path):
        return os.path.join(os.getcwd(), relative_path)

    @classmethod
    def get_path(cls, path):
        return os.path.split(path)[0]

    @classmethod
    def get_name(cls, path):
        return os.path.split(path)[1]

    @classmethod
    def get_base_name(cls, path):
        return cls.get_name(path).split('.')[0]

    @classmethod
    def get_postfix(cls, path):
        temp = cls.get_name(path).split('.')
        return None if len(temp) == 1 else temp[-1]

    @classmethod
    def start_from(cls, path ,prefix):
        return path[0 : len(prefix)] == prefix

    @classmethod
    def get_rid_of_prefix_path(cls, path, prefix):
        return path[len(prefix)+1 : ]

    @classmethod
    def get_rid_of_top_path(cls, path):
        return cls.get_rid_of_prefix_path(path, path.split(os.path.sep)[0])
        