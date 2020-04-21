import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.4559, 'linux2_py2':0.52483, 'win32_py2':0.52404,
                   'darwin_py3':0.52403, 'linux_py3':0.52403, 'win32_py3':0.52483}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['6bxx_strands-3'], expected_result=expected_result, nproc=nproc)