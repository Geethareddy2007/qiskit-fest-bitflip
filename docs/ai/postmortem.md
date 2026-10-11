# Project Postmortem — Team BitFlip

**Status:** Draft; complete after experiments finish.

## What worked
- Dependency installation succeeded using `python -m pip`.
- Processor JSON definitions loaded in Colab after adding the project root to `sys.path`.
- Exact solver reported Max-Cut value `11` and bitstring `01001`.
- A 5-qubit quantum circuit was generated.

## Problems encountered
- Windows application-control policy blocked direct `pip.exe` invocation.
- Initial Colab runtime lacked Qiskit.
- Nested project folder caused an import-path issue.
- Processor B's official qubit count/connectivity is ambiguous in the available reference.

## Limitations
- Noise values are illustrative team assumptions, not official calibration.
- Processor B's current 9-qubit chain is provisional, not a verified topology.
- Circuit visualization alone does not demonstrate solution quality.
- Do not claim one processor is superior until simulations, metrics, and assumptions are checked.

## Before submission
- [ ] Run all notebook cells from a fresh runtime.
- [ ] Verify Processor B topology against the official source.
- [ ] Confirm graph weights, bitstring ordering, and objective calculation.
- [ ] Record shots, QAOA depth, optimizer, seed, and transpilation settings.
- [ ] Save results and plots and verify reported values against output files.
- [ ] Add team members' contributions and review this document.
- [ ] Follow event rules for AI disclosure.
