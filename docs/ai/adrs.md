# Architecture Decision Records (ADRs) — Team BitFlip

Initial records based on the current project state. Review and correct them as needed.

## ADR-001: Use QAOA for Max-Cut
- **Status:** Current approach; confirm against notebook implementation.
- **Context:** The project evaluates a Max-Cut problem using a quantum circuit.
- **Decision:** Use QAOA as the candidate quantum approach.
- **Alternatives:** Exact classical Max-Cut search; other quantum optimization approaches.
- **Consequences:** Evaluate sampled bitstrings against a trusted classical optimum.
- **Verify and record:** QAOA depth, optimizer, shots, seed, and parameter-selection procedure.

## ADR-002: Store processor definitions in JSON
- **Status:** Implemented.
- **Decision:** Store qubit count, basis gates, coupling map, and noise assumptions in `processors/processor_A.json` and `processors/processor_B.json`.
- **Consequence:** Configurations are inspectable and reusable; provenance must be clear.

## ADR-003: Keep Processor B provisional
- **Status:** Open — topology verification required.
- **Context:** The reference reportedly labels Processor B as 7 qubits, while 9 circles appear in the image. The current team JSON models 9 nodes as a linear chain.
- **Decision:** Treat the 9-node chain as a working model only until the intended topology is confirmed.
- **Consequence:** Results are conditional on this assumption and are not official hardware results.
- **Next action:** Verify qubit count and every edge against the official reference or organizer clarification.

## ADR-004: Label noise assumptions as illustrative
- **Status:** Implemented.
- **Context:** The JSON uses team-assumed depolarizing and readout error probabilities.
- **Decision:** Label these values as illustrative, not official calibration data.
- **Consequence:** Noise comparisons represent model behavior, not calibrated physical-hardware performance.
