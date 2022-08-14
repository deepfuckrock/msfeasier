import sys
import subprocess

# implement pip as a subprocess:
def install():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

