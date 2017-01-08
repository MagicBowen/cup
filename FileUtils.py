import os


class FileUtils:
    @classmethod
    def get_content(cls, filename):
        with open(filename, 'r') as f:
            return f.read()

    @classmethod
    def set_content(cls, filename, content):
        with open(filename, 'w') as f: f.write(content)

    @classmethod
    def search_file_by_postfix(cls, dir, postfix):
        result = []
        for parent, dirnames, filenames in os.walk(dir):
            for file in filenames:
                if postfix in file:
                    result.append(file)
        return result
