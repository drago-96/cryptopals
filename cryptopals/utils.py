import os

lib_dir = os.path.dirname(__file__)


def load_file(filename):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, filename)
