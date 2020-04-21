import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.38521, 'linux2_py2':0.39583, 'win32_py2':0.39605,
                   'darwin_py3':0.39564, 'linux_py3':0.39514, 'win32_py3':0.39531}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_rescore_models'], expected_result=expected_result, nproc=nproc)