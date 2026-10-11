"""Plot processor coupling maps and comparison metrics."""
from pathlib import Path
import matplotlib.pyplot as plt
import networkx as nx


def plot_processor_graph(processor: dict, output_path: str | Path) -> None:
    graph = nx.Graph()
    graph.add_nodes_from(range(processor["num_qubits"]))
    graph.add_edges_from(tuple(edge) for edge in processor["coupling_map"])
    pos = nx.spring_layout(graph, seed=7)
    plt.figure(figsize=(6, 4))
    nx.draw_networkx(graph, pos=pos, with_labels=True, node_size=700)
    plt.title(f'{processor["name"]} coupling graph')
    plt.axis("off")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=180, bbox_inches="tight")
    plt.close()
