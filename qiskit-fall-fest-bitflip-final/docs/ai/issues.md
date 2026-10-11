# Issues and Resolutions — Team BitFlip

## ISSUE-001: Direct `pip.exe` invocation blocked
- **Symptom:** Windows Device Guard / application-control policy blocked direct invocation.
- **Resolution:** `python -m pip install -r requirements.txt` succeeded.
- **Status:** Resolved.
- **Note:** Do not disable system security controls.

## ISSUE-002: Qiskit missing in Colab
- **Symptom:** `ModuleNotFoundError: No module named 'qiskit'`.
- **Resolution:** Installed the project dependencies in the active Colab runtime using `%pip install`.
- **Status:** Resolved in that runtime.

## ISSUE-003: `src` package not found in Colab
- **Symptom:** `ModuleNotFoundError: No module named 'src'`.
- **Cause:** The project root was nested at `/content/qiskit-project/qiskit-fall-fest-bitflip-final`.
- **Resolution:** Added the actual project root to `sys.path`.
- **Status:** Resolved.

## ISSUE-004: Processor B topology uncertain
- **Symptom:** Reference description says 7 qubits, while 9 circles appear; current JSON uses a 9-node chain.
- **Resolution:** Marked the model provisional.
- **Status:** Open — verify before final comparison.

## ISSUE-005: Official calibration unavailable
- **Symptom:** Processor JSON contains illustrative noise probabilities.
- **Resolution:** Labeled them as team assumptions, not official calibration.
- **Status:** Open — replace only if authoritative data becomes available.
