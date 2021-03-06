import os, shutil
from fragon_regression.test_data import tests, nproc, compiler, strict
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.4696, 'linux_py2_gfortran':0.47519, 'win32_gfortran':0.47519,
                   'darwin_gfortran':0.47519, 'linux_py3_gfortran':0.47519, 'minimum':0.45}
regression_dir=os.environ['FRAGON_REGRESSION']
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  shutil.copy(os.path.join(regression_dir,'data','strands.pdb'),os.getcwd())
  run_test(test=tests['5awl_fragment'], expected_result=expected_result, compiler=compiler, strict=strict, nproc=nproc)
