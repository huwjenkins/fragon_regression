import os
from fragon_regression.test_data import tests, nproc, compiler, strict
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.40221, 'linux_py2_gfortran':0.42152, 'win32_gfortran':0.42409,
                   'darwin_gfortran':0.4184, 'linux_py3_gfortran':0.42236, 'minimum':0.39}
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  run_test(test=tests['4ubz_anti-0_solvent'], expected_result=expected_result, compiler=compiler, strict=strict, nproc=nproc)
