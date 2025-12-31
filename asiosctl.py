import sys, yaml, subprocess, os

def load():
    with open('execution_set.yaml','r') as f:
        return yaml.safe_load(f)['executors']

def run(name):
    ex = load()[name]
    cwd = os.path.abspath(ex.get('workdir','.'))
    entry = ex['entry']
    if ex.get('type') == 'module':
        cmd = [sys.executable, '-m', entry]
    else:
        cmd = [sys.executable, entry]
    subprocess.check_call(cmd, cwd=cwd)

if __name__ == '__main__':
    if sys.argv[1] == 'run':
        run(sys.argv[2])
