# -*- coding:utf-8 -*-
import os

FILE_DIR = '/file'


def make_file_dir(path):
    if not os.path.exists(path):
        print u"创建目录" + path
        os.mkdir(path)
    else:
        print u"目录" + path + u"已存在"

        # basedir = os.path.abspath(os.path.dirname(__file__))
