# ASIOS Execution Set — Canonical Execution Substrate

Authoritative, public execution manifest for ASIOS / Aureon.

This repository defines the **runnable executors only**: their entrypoints, inputs, and deterministic outputs.  
No submissions, proofs, or audit artifacts live here.

## Purpose

- Single source of truth for executable agents
- Deterministic execution surface
- Verifiable inputs and outputs
- Stable substrate for higher-level audit and proof repositories

## Scope

Included:
- Executable agents and tools
- Orchestrators and runners
- Deterministic execution configs
- CI validation for executability


## Guarantees

- Executable determinism
- Frozen operational boundaries
- Reproducible runs from declared inputs
- Clean separation from audit and proof layers

## Relationship to Other Repositories

- **asios-execution-set**  
  Execution only. No evidence.

- **aureon-swarm-proof**  
  Proof, hashes, audits, verification.

This separation is intentional and enforced.

## Status

Canonical execution substrate.  
Required by downstream verification systems.
