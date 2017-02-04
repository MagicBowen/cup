import os


class FileUtils:
    @classmethod
    def get_content(cls, file):
        with open(file, 'r') as f:
            return f.read()

    @classmethod
    def fullfill(cls, file, content):
        path, _ = os.path.split(file)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(file, 'w') as f: f.write(content)