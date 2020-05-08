import os, shutil
from fragon_regression.test_data import tests, nproc, compiler
from fragon_regression.test_runner import run_test
expected_result = {'darwin_ifort':0.46673, 'linux2_gfortran':0.47434, 'win32_gfortran':0.47434,
                   'darwin_gfortran':0.47434}
regression_dir=os.environ['FRAGON_REGRESSION']
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  shutil.copy(os.path.join(regression_dir,'data','strands.pdb'),os.getcwd())
  run_test(test=tests['5awl_fragment_I+I-'], expected_result=expected_result, compiler=compiler, nproc=nproc)
