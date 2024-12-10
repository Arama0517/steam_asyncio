import shutil

from tools import current_dir

shutil.rmtree(current_dir / 'dist')
shutil.rmtree(current_dir / 'steam.egg-info')
