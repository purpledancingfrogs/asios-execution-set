import yaml, subprocess, sys

with open('execution_set.yaml') as f:
    cfg = yaml.safe_load(f)

def list_exec():
    for e in cfg['executors']:
        print(f\"{e['name']} -> {e['entrypoint']}\")
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: asiosctl list')
        sys.exit(1)
    if sys.argv[1] == 'list':
        list_exec()
