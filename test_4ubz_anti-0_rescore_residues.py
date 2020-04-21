import os
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.35869, 'linux2_py2':0.42438, 'win32_py2':0.43811,
                   'darwin_py3':0.37149, 'linux_py3':0.41165, 'win32_py3':0.3548}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_rescore_residues'], expected_result=expected_result, nproc=nproc)