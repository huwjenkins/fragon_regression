import os, shutil
from fragon_regression.test_data import tests, nproc
from fragon_regression.test_runner import run_test
expected_result = {'darwin_py2':0.46673, 'linux2_py2':0.47434, 'win32_py2':0.47434,
                   'darwin_py3':0.47434, 'linux_py3':0.47434, 'win32_py3':0.47434}
regression_dir=os.environ['FRAGON_REGRESSION']
def test(tmpdir):
  os.chdir(tmpdir.strpath)
  shutil.copy(os.path.join(regression_dir,'data','strands.pdb'),os.getcwd())
  run_test(test=tests['5awl_fragment_I+I-'], expected_result=expected_result, nproc=nproc)