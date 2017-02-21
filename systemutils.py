import os
import subprocess


class SystemUtils:
    @classmethod
    def exec(cls, cmd):
        status, output = subprocess.getstatusoutput(cmd)
        print(output)
        if status != 0:
            raise Exception("execute '%s' failed" % cmd)

    @classmethod
    def find_file_by_name(cls, path, filename):
        for file in os.listdir(path):
            fp = os.path.join(path, file)
            print(file)
            print(fp)
            if os.path.isfile(fp) and file == filename:
                return fp
            elif os.path.isdir(fp):
                result =  cls.find_file_by_name(fp, filename) 
                if result is not None : return result
        return None       