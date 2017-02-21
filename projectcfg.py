import os
import configparser



class ProjectConfig:
    def __init__(self, file):
        self.file = file
        self.parser = configparser.ConfigParser()

    def get(self, section, key):
        try:
            self.parser.read(self.file)
            return self.parser.get(section, key)
        except Exception as e:
            return None


