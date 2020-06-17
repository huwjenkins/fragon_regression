import os
from fragon_regression.test_data import tests, nproc, compiler, strict
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.27019, 'linux_py2_gfortran':0.27767, 'win32_gfortran':0.27767,
                   'darwin_gfortran':0.27767, 'linux_py3_gfortran':0.27767, 'minimum':0.25}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['2f4k_helix6'], expected_result=expected_result, compiler=compiler, strict=strict, nproc=nproc)
