from __future__ import print_function, division, absolute_import

import os
import sys
from os.path import abspath, expanduser, join

import conda.config as cc


from functools import total_ordering

@total_ordering
class _int(object):
    """
    Mutable int.

    Allows CONDA_PY to be modified globally without restarting conda. Modify
    by changing the ``i`` attribute.

    """
    def __init__(self, arg):
        self.i = int(arg)

    def __int__(self):
        return self.i

    def __lt__(self, other):
        if isinstance(other, _int):
            return self.i < other.i
        return self.i < other

    def __str__(self):
        return str(self.i)

    def __repr__(self):
        return repr(self.i)

CONDA_PY = _int(os.getenv('CONDA_PY', cc.default_python.replace('.', '')))
CONDA_NPY = _int(os.getenv('CONDA_NPY', 17))
PY3K = int(bool(CONDA_PY >= 30))

if cc.root_writable:
    croot = join(cc.root_dir, 'conda-bld')
else:
    croot = abspath(expanduser('~/conda-bld'))

build_prefix = join(cc.envs_dirs[0], '_build')
test_prefix = join(cc.envs_dirs[0], '_test')

def _get_python(prefix):
    if sys.platform == 'win32':
        res = join(prefix, 'python.exe')
    else:
        res = join(prefix, 'bin/python')
    return res

build_python = _get_python(build_prefix)
test_python = _get_python(test_prefix)


def show():
    import conda.config as cc

    print('CONDA_PY:', CONDA_PY)
    print('CONDA_NPY:', CONDA_NPY)
    print('subdir:', cc.subdir)
    print('croot:', croot)
