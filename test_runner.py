from __future__ import division, print_function
import sys, subprocess, shlex, json

def read_results_json(results_json):
  with open(results_json,'r') as results:
    loaded_results = json.load(results)
  loaded_results['name'] = str(loaded_results['name'])
  for solution in loaded_results['solutions']:
    solution['id'] = str(solution['id'])
  return loaded_results

def get_fragon_exe():
  import fragon.version
  if 'py2' in fragon.__file__:
    fragon = 'fragon'
  elif 'cctbx' in fragon.__file__:
    fragon = 'cctbx.fragon'
  else:
    fragon = 'fragon'
  if sys.platform.startswith('win'):
    fragon += '.bat'
  return fragon

def run_test(test, expected_result, compiler, nproc):
  fragon_command_line = get_fragon_exe()
  fragon_command_line += ' --mtz {}'.format(test['data'])
  if test['seq'] is not None:
    fragon_command_line += ' --seq {}'.format(test['seq'])
  fragon_command_line += test['search']
  fragon_command_line += ' --solutions 100'
  fragon_command_line += ' --nproc {}'.format(nproc)
  run_fragon = shlex.split(fragon_command_line, posix=False)
  fragon_logfile = test['log_root'] + '_stdout.log'
  fragon_stderrfile = test['log_root'] + '_stderr.log'
  fragon_log = open(fragon_logfile, 'w')
  fragon_stderr = open(fragon_stderrfile, 'w')
  fragon_process = subprocess.Popen(run_fragon, stdout=fragon_log, stderr=fragon_stderr)
  fragon_process.communicate()
  try:
    result = sorted([solution for solution in read_results_json(test['results_json'])['solutions'] if solution['acornCC'] is not None], key=lambda r: r['acornCC'],reverse=True)[0]
  except (IOError, KeyError) as e:
    with open(fragon_stderrfile, 'r') as f:
      print(f.read(), file=sys.stderr)
    raise(e)
  assert result['acornCC'] is not None
  assert result['acornCC'] == expected_result['_'.join([sys.platform, compiler])]
