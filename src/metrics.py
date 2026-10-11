"""Architecture and experiment metrics."""
import math


def circuit_metrics(circuit) -> dict:
    ops = circuit.count_ops()
    two_qubit_names = {"cx", "cz", "ecr", "swap", "rxx", "ryy", "rzz"}
    return {
        "depth": circuit.depth(),
        "num_qubits": circuit.num_qubits,
        "total_ops": int(sum(ops.values())),
        "two_qubit_ops_estimate": int(sum(n for gate, n in ops.items() if gate.lower() in two_qubit_names)),
        "swap_count": int(ops.get("swap", 0)),
        "operations": {str(k): int(v) for k, v in ops.items()},
    }


def proportion_standard_error(p: float, n: int) -> float:
    if n <= 0 or not 0 <= p <= 1:
        raise ValueError("Require n > 0 and 0 <= p <= 1")
    return math.sqrt(p * (1 - p) / n)
