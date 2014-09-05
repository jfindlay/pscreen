#!/usr/bin/env python

import os
from distutils.core import setup
from subprocess import Popen,PIPE

def test_screen():
  for path in re.split(':',os.environ['PATH']):
    if os.path.exists(os.path.join(path,'screen')):
      return
  sys.stderr.write('GNU screen not found.\n') ; sys.stderr.flush()
  sys.exit(1)

def get_version():
  return str(Popen(('git describe --tags'.split()),stdout=PIPE).stdout.read().strip())

def get_files(dirname):
  '''
  dirname is relative to source directory
  '''
  src_dir = os.path.dirname(os.path.realpath(__file__))
  prof_dir = os.path.join(src_dir,dirname)
  profs = []
  for prof in os.listdir(prof_dir):
    if os.path.isfile(os.path.join(prof_dir,prof)):
      profs.append(os.path.join(dirname,prof))
  return profs

setup(
    name='pscreen',
    version=get_version(),
    description='manage and interface with multiple screen profiles easily',
    author='Justin Findlay',
    author_email='jfindlay@gmail.com',
    url='http://github.com/jfindlay/pscreen/',
    scripts=('utils/pscreen',),
    data_files=[('share/pscreen/profiles',get_files('profiles'))]
    )
