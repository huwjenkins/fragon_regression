import os
from fragon_regression.test_data import tests, nproc, compiler
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.40953, 'linux_gfortran':0.42889, 'win32_gfortran':0.4302,
                   'darwin_gfortran':0.43337}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_rescore_strands'], expected_result=expected_result, compiler=compiler, nproc=nproc)
