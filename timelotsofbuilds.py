import sys
import subprocess
import os
import shutil
import time

def main():
    shutil.rmtree('/Users/aaronmeurer/Desktop/testchannel')
    move_package_to_channel(400)
    for i in range(100):
        print('copying')
        move_package_to_channel(i)
        t = time_conda_install()
        print(i, t)
        with open('lotsofbuildstimes', 'a') as f:
            f.write("%s %s\n" % (i, t))

def move_package_to_channel(n):
    try:
        os.makedirs('/Users/aaronmeurer/Desktop/testchannel/osx-64')
    except FileExistsError:
        pass
    shutil.copy2(os.path.expanduser("~/anaconda/conda-bld/osx-64/lotsofbuilds-1.0-%d.tar.bz2"
        % n), os.path.expanduser("~/Desktop/testchannel/osx-64"))
    shutil.copy2(os.path.expanduser("~/anaconda/conda-bld/osx-64/testpackage-1.0-0.tar.bz2"),
        os.path.expanduser("~/Desktop/testchannel/osx-64"))
    subprocess.check_call(['conda', 'index', os.path.expanduser('~/Desktop/testchannel/osx-64')])

def time_conda_install():
    t = time.time()
    subprocess.check_call(['conda', '--debug', 'create', '-n', 'test', '-c',
        'file:///Users/aaronmeurer/Desktop/testchannel', '--override',
        'lotsofbuilds', '--dry'])
    return time.time() - t

if __name__ == "__main__":
    sys.exit(main())
