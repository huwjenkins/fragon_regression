import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.40953, 'linux2_py2':0.42889, 'win32_py2':0.4302, 
                   'darwin_py3':0.43337, 'linux_py3':0.43329, 'win32_py3':0.43443}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_rescore_strands'], expected_result=expected_result, nproc=nproc)