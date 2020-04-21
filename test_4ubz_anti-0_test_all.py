import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.41025, 'linux2_py2':0.42843, 'win32_py2':0.42822,
                   'darwin_py3':0.42805, 'linux_py3':0.42808, 'win32_py3':0.4282}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_test_all'], expected_result=expected_result, nproc=nproc)