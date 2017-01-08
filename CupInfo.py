import os


class CupInfo:
    cup_root = ''
    template_path = ''

    @classmethod
    def load(cls):
        cls.cup_root = os.path.dirname(os.path.abspath(__file__))
        cls.template_path = os.path.join(cls.cup_root, 'template')