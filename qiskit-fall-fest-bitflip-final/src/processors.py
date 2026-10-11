"""Load and validate processor model JSON files."""
from pathlib import Path
import json
from typing import Any


def load_processor(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        config = json.load(handle)
    validate_processor(config)
    return config


def validate_processor(config: dict[str, Any]) -> None:
    n = config.get("num_qubits")
    edges = config.get("coupling_map")
    if not isinstance(n, int) or n < 1:
        raise ValueError("num_qubits must be a positive integer")
    if not isinstance(edges, list):
        raise ValueError("coupling_map must be a list of [u, v] pairs")
    seen = set()
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError(f"Invalid coupling edge: {edge!r}")
        u, v = edge
        if not isinstance(u, int) or not isinstance(v, int):
            raise ValueError(f"Qubit indices must be integers: {edge!r}")
        if u == v or min(u, v) < 0 or max(u, v) >= n:
            raise ValueError(f"Edge references invalid qubit: {edge!r}")
        canonical = tuple(sorted((u, v)))
        if canonical in seen:
            raise ValueError(f"Duplicate undirected edge: {edge!r}")
        seen.add(canonical)
