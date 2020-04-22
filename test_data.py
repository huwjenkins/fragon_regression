import os
regression_dir=os.environ['FRAGON_REGRESSION']
data_dir=os.path.join(regression_dir,'data')
nproc = 4
tests={'5mas_helix7':{
          'test_case':'5mas',
          'data':os.path.join(data_dir, '5mas_1.1A.mtz'),
          'seq':os.path.join(data_dir, '5mas.seq'),
          'search':' --name 5mas --helix 7 --search_highres 1.5',
          'log_root':'5mas_helix7',
          'results_json':'5mas_Fragon_1x_helix7.json'
          },
       '2f4k_helix6':{
          'test_case':'2f4k',
          'data':os.path.join(data_dir,'2f4k.mtz'),
          'seq':os.path.join(data_dir,'2f4k.seq'),
          'search':' --helix 6',
          'log_root':'2f4k_helix6',
          'results_json':'2f4k_Fragon_1x_helix6.json'
          },
       '4ubz_anti-0':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':os.path.join(data_dir, '4ubz.seq'),
          'search':' --ensemble {}'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '4ubz_anti-0_rescore_strands':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':os.path.join(data_dir, '4ubz.seq'),
          'search':' --ensemble {} --rescore_strands --ACORN_definitive_CC 0.41'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0_rescore_strands',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '4ubz_anti-0_rescore_residues':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':os.path.join(data_dir, '4ubz.seq'),
          'search':' --ensemble {} --rescore_residues --test_all'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0_rescore_residues',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '4ubz_anti-0_rescore_models':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':os.path.join(data_dir, '4ubz.seq'),
          'search':' --ensemble {} --rescore_models --ACORN_definitive_CC 0.41'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0_rescore_models',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '4ubz_anti-0_solvent':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':None,
          'search':' --solvent 0.5 --ensemble {}'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0_solvent',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '4ubz_anti-0_test_all':{
          'test_case':'4ubz',
          'data':os.path.join(data_dir, '4ubz.mtz'),
          'seq':os.path.join(data_dir, '4ubz.seq'),
          'search':' --ensemble {} --test_all'.format(os.path.join(data_dir, 'anti_0-strands-5.pdb')),
          'log_root':'4ubz_anti-0_test_all',
          'results_json':'4ubz_Fragon_1x_anti_0-strands-5.json'
          },
       '5awl_fragment':{
          'test_case':'5awl',
          'data':os.path.join(data_dir, '5awl.mtz'),
          'seq':os.path.join(data_dir, '5awl.seq'),
          'search':' --name 5awl --fragment strands.pdb',
          'log_root':'5awl_fragment',
          'results_json':'5awl_Fragon_1x_strands.json',
          },
       '5awl_fragment_I+I-':{
          'test_case':'5awl',
          'data':os.path.join(data_dir, '5awl_I+I-.mtz'),
          'seq':os.path.join(data_dir, '5awl.seq'),
          'search':' --name 5awl --fragment strands.pdb',
          'log_root':'5awl_fragment_I+I-',
          'results_json':'5awl_Fragon_1x_strands.json',
          },
       '6bxx_strands-3':{
          'test_case':'6bxx',
          'data':os.path.join(data_dir, '6bxx_1.15A.mtz'),
          'seq':os.path.join(data_dir, '6bxx.seq'),
          'search':' --name 6bxx --ensemble {}'.format(os.path.join(data_dir, 'strands-3.pdb')),
          'log_root':'6bxx_strands-3',
          'results_json':'6bxx_Fragon_1x_strands-3.json',
          },
       '6bxx_strands-3_all_P222':{
          'test_case':'6bxx',
          'data':os.path.join(data_dir, '6bxx_P222_1.15A.mtz'),
          'seq':os.path.join(data_dir, '6bxx.seq'),
          'search':' --name 6bxx --ensemble {} --test_all_plausible_sg'.format(os.path.join(data_dir, 'strands-3.pdb')),
          'log_root':'6bxx_strands-3',
          'results_json':'6bxx_Fragon_1x_strands-3.json',
          },
       }