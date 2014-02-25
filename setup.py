#!/usr/bin/env python

from distutils.core import setup
from subprocess import Popen,PIPE

def test_screen():
  for path in re.split(':',os.environ['PATH']):
    if os.path.exists(os.path.join(path,'screen')):
      return
  sys.stderr.write('GNU screen not found.\n') ; sys.stderr.flush()
  sys.exit(1)

def get_version():
  return Popen(('git','describe'),stdout=PIPE).stdout.read()

setup(
    name='pscreen',
    version=get_version(),
    description='Python Distribution Utilities',
    author='Justin Findlay',
    author_email='jfindlay@gmail.com',
    url='http://github.com/jfindlay/pscreen/',
    )
