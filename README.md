# ASIOS Execution Set

Canonical, auditable execution manifest for Aureon / ASIOS.

## Overview
This repository defines the authoritative **execution set**: a deterministic map of runnable executors, their entrypoints, and working directories.  
It is the bridge between governed intent and concrete execution.

## Structure
- execution_set.yaml — declarative executor registry
- siosctl.py — unified controller
- .github/workflows/ — CI validation
- Executors live in sibling folders:
  - decision-decomposition
  - QuantumMeasurementContradictionKit
  - ecursive-paradox-governance

## Usage

Run an executor:
`ash
python asiosctl.py run decision-decomposition
python asiosctl.py run qmck
``

## Guarantees

* Explicit entrypoints
* Deterministic working directories
* CI-validated executability

This execution set is canonical. Changes must be committed and audited.
