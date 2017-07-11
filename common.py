import os


def make_file_dir():
    basedir = os.path.abspath(os.path.dirname(__file__))
    all_file_dir = basedir + '/file'
    if not os.path.exists(all_file_dir):
        os.mkdir(all_file_dir)
