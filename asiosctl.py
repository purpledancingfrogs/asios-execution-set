import sys
import yaml
import subprocess
from pathlib import Path

def load():
    with open("execution_set.yaml") as f:
        return yaml.safe_load(f)

def list_execs():
    for k in load()["executors"]:
        print(k)

def run(name):
    cfg = load()["executors"][name]
    path = Path(cfg["path"]).resolve()
    entry = cfg["entry"]
    cmd = [sys.executable, entry] if entry.endswith(".py") else [entry]
    subprocess.check_call(cmd, cwd=path)

if __name__ == "__main__":
    if sys.argv[1] == "list":
        list_execs()
    elif sys.argv[1] == "run":
        run(sys.argv[2])
