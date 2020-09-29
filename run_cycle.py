import os
import time
from pathlib import Path

topdir = Path(os.path.dirname(__file__))

os.system('python3 make_test.py')
time.sleep(1)
os.system('python3 take_test.py')
os.system(f'cd {topdir}')
os.system('pwd')
os.system('python3 mark_tests.py')
