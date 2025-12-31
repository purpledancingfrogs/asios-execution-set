import sys, yaml, subprocess, pathlib

def load():
    with open('execution_set.yaml') as f:
        return yaml.safe_load(f)['executors']

def run(name):
    ex = load()[name]
    path = pathlib.Path(ex['path'])
    entry = ex['entry']
    subprocess.check_call([sys.executable, entry], cwd=path)

def main():
    if sys.argv[1] == 'list':
        print('\\n'.join(load().keys()))
    if sys.argv[1] == 'run':
        run(sys.argv[2])

if __name__ == '__main__':
    main()
