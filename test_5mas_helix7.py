import os
from fragon_regression.test_data import tests, nproc, compiler, strict
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.61251, 'linux_py2_gfortran':0.62390, 'win32_gfortran':0.62390,
                   'darwin_gfortran':0.62390, 'linux_py3_gfortran':0.62390, 'minimum':0.6}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['5mas_helix7'], expected_result=expected_result, compiler=compiler, strict=strict, nproc=nproc)
