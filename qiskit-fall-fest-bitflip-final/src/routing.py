"""Helpers for comparing a logical circuit with processor-transpiled circuits."""
from qiskit import transpile


def compile_for_processor(circuit, processor: dict, seed_transpiler: int = 42):
    """Transpile against a coupling map; processor noise is not automatically applied."""
    return transpile(
        circuit,
        basis_gates=processor.get("basis_gates"),
        coupling_map=processor["coupling_map"],
        optimization_level=3,
        seed_transpiler=seed_transpiler,
    )
