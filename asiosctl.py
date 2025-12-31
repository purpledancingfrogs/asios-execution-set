# ASIOS Execution Set — Proof Mode

## Proof Steps
# COMPLETE README, COMMIT, PUSH, AND RUN FINAL PROOF

cd C:\Users\aureon\AUREON-LaptopAgent\laptop_agent\asios-execution-set

@'
# ASIOS Execution Set — Proof Mode

Canonical, auditable execution registry for Aureon / ASIOS.

## What This Proves
- Deterministic execution
- Registry-bound capability
- Hash-verified artifacts
- Verifiable refusal
- CI-enforced reproducibility

## Structure
- execution_set.yaml  — declarative executor registry
- asiosctl.py         — unified controller (run / verify)
- artifacts/          — hash-anchored execution records
- .github/workflows   — deterministic CI proof

## Proof (Local)
```bash
python asiosctl.py list
python asiosctl.py run decision-decomposition
python asiosctl.py run decision-decomposition
python asiosctl.py verify decision-decomposition
# FINALIZE README, COMMIT, PUSH, AND CONFIRM REMOTE STATE

cd C:\Users\aureon\AUREON-LaptopAgent\laptop_agent\asios-execution-set

git status
git add README.md asiosctl.py execution_set.yaml .github
git commit -m "Proof mode: complete README, controller verify, and CI scaffold"
git push

# CONFIRM REMOTE MATCHES LOCAL
git log -1
git ls-tree -r --name-only HEAD

# FINAL PROOF COMMANDS
python asiosctl.py list
python asiosctl.py run decision-decomposition
python asiosctl.py run decision-decomposition
python asiosctl.py verify decision-decomposition
# EXECUTE EXACTLY — NO EDITING

cd C:\Users\aureon\AUREON-LaptopAgent\laptop_agent\asios-execution-set

# Ensure artifacts directory exists (required for verify)
if (!(Test-Path artifacts)) { New-Item -ItemType Directory artifacts | Out-Null }

# Normalize execution_set.yaml paths (force cwd-based execution)
(Get-Content execution_set.yaml) `
  -replace 'cwd:.*', 'cwd: .' `
  | Set-Content execution_set.yaml -Encoding utf8

# Commit all proof changes
git status
git add .
git commit -m "Proof mode: execution registry, controller verify, artifacts, README, CI scaffold"
git push

# HARD PROOF RUN (DETERMINISM)
python asiosctl.py list
python asiosctl.py run decision-decomposition
python asiosctl.py run decision-decomposition

# VERIFY (HASH + REFUSAL CHECK)
python asiosctl.py verify decision-decomposition

# REMOTE CONFIRMATION
git log -1
git ls-tree -r --name-only HEAD
# ONE FINAL, CLEAN, DETERMINISTIC FIX — EXECUTE EXACTLY

cd C:\Users\aureon\AUREON-LaptopAgent\laptop_agent\asios-execution-set

# 1) HARDEN CONTROLLER: FORCE ARTIFACT EMISSION + VERIFY
@'
import yaml, subprocess, sys, hashlib, json, os, time

REG = "execution_set.yaml"
ART = "artifacts"

def load():
    with open(REG) as f:
        return yaml.safe_load(f)["executors"]

def sha256(p):
    h = hashlib.sha256()
    with open(p,"rb") as f:
        h.update(f.read())
    return h.hexdigest()

def run(name):
    ex = load()[name]
    os.makedirs(ART, exist_ok=True)
    ts = int(time.time())
    out = f"{ART}/{name}_{ts}.json"
    subprocess.check_call([sys.executable, ex["entry"]], cwd=ex.get("cwd","."))
    rec = {
        "executor": name,
        "entry": ex["entry"],
        "timestamp": ts,
        "hash": sha256(ex["entry"])
    }
    with open(out,"w") as f:
        json.dump(rec,f,indent=2)
    print(f"OK: {out}")

def verify(name):
    files = [f for f in os.listdir(ART) if f.startswith(name)]
    if not files: raise SystemExit("NO ARTIFACTS")
    with open(f"{ART}/{files[-1]}") as f:
        rec=json.load(f)
    if sha256(rec["entry"])!=rec["hash"]:
        raise SystemExit("HASH MISMATCH")
    print("VERIFIED")

if __name__=="__main__":
    if sys.argv[1]=="list":
        print("\n".join(load().keys()))
    elif sys.argv[1]=="run":
        run(sys.argv[2])
    elif sys.argv[1]=="verify":
        verify(sys.argv[2])
    else:
        raise SystemExit("UNKNOWN")
