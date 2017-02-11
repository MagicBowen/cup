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
    def replace_file(cls, source, target, replace):
        if target == source: 
            raise Exception('target %s should not be equal to source %s' % (target, source))
        cls.create_file(target)
        with open(source, 'r') as src:
            with open(target, 'w') as dst:
                for line in src:
                    dst.write(cls.__replace_line_by(line, replace))

    @classmethod
    def __replace_line_by(cls, line, replace):
        for key in replace.keys():
            line.replace(key, replace[key])

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