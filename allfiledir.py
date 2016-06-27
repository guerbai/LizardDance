import os

basedir = os.path.abspath(os.path.dirname(__file__))
allfilrdir = basedir + '/all'
if not os.path.exists(allfilrdir):
    os.mkdir(allfilrdir)