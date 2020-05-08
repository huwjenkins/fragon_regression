import os
from fragon_regression.test_data import tests, nproc, compiler
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.35869, 'linux2_gfortran':0.42438, 'win32_gfortran':0.43811,
                   'darwin_gfortran':0.37149}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_rescore_residues'], expected_result=expected_result, compiler=compiler, nproc=nproc)
