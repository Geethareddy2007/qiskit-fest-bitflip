
"""Generate the nine-node working model for Processor B.

The organizer's diagram labels Processor B as 7 qubits but visibly depicts
9 circles. This file follows the team's requested 9-node interpretation.
The coupling map is manually transcribed from the diagram and must be
verified before presenting results as official.

Run from the project root:
    python processor_B.py
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "processors" / "processor_B.json"

PROCESSOR_B = {
    "name": "Processor B",
    "num_qubits": 9,
    "coupling_map": [
        [0, 1],  # leftmost — upper-left
        [1, 2],  # upper-left — top-left
        [2, 3],  # top-left — upper-center
        [3, 4],  # upper-center — top-right
        [4, 5],  # top-right — rightmost
        [5, 6],  # rightmost — lower-right
        [6, 7],  # lower-right — center
        [7, 8],  # center — bottom
    ],
    "basis_gates": ["rz", "sx", "x", "cx"],
    "ports": [],
    "noise": {
        "type": "illustrative_depolarizing_and_readout",
        "source": "team_assumption_not_official_calibration",
        "single_qubit_depolarizing_probability": 0.001,
        "two_qubit_depolarizing_probability": 0.01,
        "readout_error_probability": 0.02,
    },
    "definition_status": (
        "TEAM_WORKING_MODEL_9_VISIBLE_NODES; "
        "connectivity_and_noise_require_verification"
    ),
}


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(
        json.dumps(PROCESSOR_B, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {OUTPUT}")
    print("WARNING: This is a provisional 9-node model, not a verified official definition.")


if __name__ == "__main__":
    main()
