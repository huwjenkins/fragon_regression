import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.40221, 'linux2_py2':0.42152, 'win32_py2':0.42409,
                   'darwin_py3':0.4184, 'linux_py3':0.42236, 'win32_py3':0.4241}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_solvent'], expected_result=expected_result, nproc=nproc)