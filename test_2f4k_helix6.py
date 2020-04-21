import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.27019, 'linux2_py2':0.27767, 'win32_py2':0.27767,
                   'darwin_py3':0.27767, 'linux_py3':0.27767, 'win32_py3':0.27767}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['2f4k_helix6'], expected_result=expected_result, nproc=nproc)