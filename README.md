# BitFlip — Qiskit Fall Fest 2026 Phase 1

**Problem:** Weighted Max-Cut with QAOA (team-created instance; replace with the official Challenge Kit instance if supplied).

## Repository structure

- `main.ipynb` — end-to-end experiment notebook (to be completed and checked before submission)
- `processor_A.py`, `processor_B.py` — generate processor JSON definitions
- `processors/` — generated processor configurations
- `src/` — reusable problem, processor, routing, metrics and visualization code
- `results/tables/`, `results/figures/` — machine-readable outputs and plots
- `report.md` — interpretation and limitations

## Setup

```bash
python -m pip install -r requirements.txt
python processor_A.py
python processor_B.py
```

## Critical verification note

Processor A's topology is transcribed from the organizer reference image. The supplied reference labels Processor B as 7 qubits but visually appears to contain more than seven nodes. The current `processor_B.py` therefore contains a **provisional team approximation**, not a verified official coupling map. Confirm the exact official Processor B specification before treating any A/B comparison as final. The noise parameters are illustrative assumptions, not device calibration data.

The weighted graph in `src/problem.py` is the team's working test instance and must be replaced if the official Challenge Kit specifies another instance.

## Reproducibility and AI disclosure

Record package versions, seeds, shots, transpiler settings, noise assumptions, and all measured metrics. The team must review and understand the generated code and disclose AI assistance if required by the organizers.
