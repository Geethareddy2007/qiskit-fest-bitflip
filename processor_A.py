"""Generate the Processor A JSON model for the QFF Phase 1 experiment.

The 5-qubit coupling graph follows the supplied reference diagram:
0--1, 0--2, 0--3, 3--4.
Noise values are explicitly illustrative unless confirmed by the official Challenge Kit.
Run: python processor_A.py
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "processors" / "processor_A.json"

PROCESSOR_A = {
    "name": "Processor A",
    "num_qubits": 5,
    "coupling_map": [[0, 1], [0, 2], [0, 3], [3, 4]],
    "basis_gates": ["rz", "sx", "x", "cx"],
    "ports": [],
    "noise": {
        "type": "illustrative_depolarizing_and_readout",
        "source": "team_assumption_not_official_calibration",
        "single_qubit_depolarizing_probability": 0.001,
        "two_qubit_depolarizing_probability": 0.01,
        "readout_error_probability": 0.02,
    },
    "definition_status": "topology_transcribed_from_organizer_reference_image; noise_is_illustrative",
}


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(PROCESSOR_A, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
