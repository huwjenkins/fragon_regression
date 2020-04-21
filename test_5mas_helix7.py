import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.61251, 'linux2_py2':0.62390, 'win32_py2':0.62390,
                   'darwin_py3':0.6239, 'linux_py3':0.62390, 'win32_py3':0.62390}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['5mas_helix7'], expected_result=expected_result, nproc=nproc)