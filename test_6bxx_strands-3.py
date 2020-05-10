import os
from fragon_regression.test_data import tests, nproc, compiler
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.4559, 'linux_py2_gfortran':0.52483, 'win32_gfortran':0.52404,
                   'darwin_gfortran':0.52403, 'linux_py3_gfortran':0.52403}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['6bxx_strands-3'], expected_result=expected_result, compiler=compiler, nproc=nproc)
