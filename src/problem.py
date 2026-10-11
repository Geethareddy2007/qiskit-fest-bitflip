"""Weighted Max-Cut instance and exact classical baseline."""
from itertools import product

NUM_VERTICES = 5
EDGES = [
    (0, 1, 2), (0, 2, 1), (1, 2, 3), (1, 3, 2),
    (2, 3, 1), (3, 4, 2), (2, 4, 2),
]


def cut_value(bits, edges=EDGES) -> int:
    return sum(weight for u, v, weight in edges if bits[u] != bits[v])


def exact_max_cut(num_vertices=NUM_VERTICES, edges=EDGES) -> dict:
    candidates = [(cut_value(bits, edges), bits) for bits in product((0, 1), repeat=num_vertices)]
    best_value = max(value for value, _ in candidates)
    best_bits = next(bits for value, bits in candidates if value == best_value)
    return {
        "optimal_cut_value": best_value,
        "optimal_bitstring": "".join(map(str, best_bits)),
        "total_edge_weight": sum(w for _, _, w in edges),
    }
