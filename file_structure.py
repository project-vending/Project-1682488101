
import os

# create the directory structure
base_dir = './realtime_processing_goes_data'
os.makedirs(base_dir)
os.makedirs(os.path.join(base_dir, 'data'))
os.makedirs(os.path.join(base_dir, 'processed_data'))

# create empty files
open(os.path.join(base_dir, 'app.py'), 'w').close()
open(os.path.join(base_dir, 'config.py'), 'w').close()
open(os.path.join(base_dir, 'requirements.txt'), 'w').close()
open(os.path.join(base_dir, 'README.md'), 'w').close()
open(os.path.join(base_dir, 'data', '.gitignore'), 'w').close()
open(os.path.join(base_dir, 'processed_data', '.gitignore'), 'w').close()
