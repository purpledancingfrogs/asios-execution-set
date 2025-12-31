import yaml, subprocess, sys, os

with open('execution_set.yaml') as f:
    cfg = yaml.safe_load(f)['execution_set']

def run(name):
    if name not in cfg:
        raise SystemExit(f'Unknown executor: {name}')
    ex = cfg[name]
    path = ex['path']
    entry = ex['entrypoint']
    os.chdir(path)
    subprocess.check_call([sys.executable, entry] if entry.endswith('.py') else [entry])

if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] != 'run':
        raise SystemExit('usage: asiosctl run <executor>')
    run(sys.argv[2])
