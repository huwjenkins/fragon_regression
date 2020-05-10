import os
from fragon_regression.test_data import tests, nproc, compiler
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.41025, 'linux_py2_gfortran':0.42843, 'win32_gfortran':0.42822,
                   'darwin_gfortran':0.42805, 'linux_py3_gfortran':0.42808}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_test_all'], expected_result=expected_result, compiler=compiler, nproc=nproc)
