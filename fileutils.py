import os


class FileUtils:
    @classmethod
    def get_content(cls, file):
        with open(file, 'r') as f:
            return f.read()

    @classmethod
    def create_file(cls, file):
        cls.fullfill(file, '')

    @classmethod
    def fullfill(cls, file, content):
        path, _ = os.path.split(file)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(file, 'w') as f: f.write(content)

    @classmethod
    def get_rid_of_prefix_path(cls, path, prefix):
        return path[len(prefix)+1 : ]

    @classmethod
    def get_rid_of_top_path(cls, path):
        return cls.get_rid_of_prefix_path(path, path.split(os.path.sep)[0])