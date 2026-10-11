# Plan Evolution — Team BitFlip

Initial timeline based on the setup and outputs recorded so far. Update with actual dates and team decisions.

## Stage 1 — Environment
- Dependencies installed.
- Project opened in Google Colab after a local Windows application-control issue.
- Nested project root added to Python's import path.

## Stage 2 — Problem verification
- Exact Max-Cut solver reported optimum value `11`.
- Reported optimal bitstring: `01001`.
- Sample cut `[0, 1, 0, 0, 1]` was reported with value `11`.
- Confirm bitstring ordering and graph-scoring convention in the implementation.

## Stage 3 — Circuit generation
- A 5-qubit QAOA-style circuit was generated.
- Next: run remaining notebook cells and capture actual simulation metrics.

## Stage 4 — Processor comparison
- Processor A: 5 qubits; edges `[[0,1],[0,2],[0,3],[3,4]]`.
- Processor B: provisional 9-node chain.
- Verify Processor B topology and document routing, transpilation, and simulation settings before final results.

## Update format
For each major change, record the date, previous plan, new decision, evidence, and expected impact.
