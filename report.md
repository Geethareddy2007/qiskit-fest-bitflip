# Phase 1 Report — BitFlip

## Problem statement
Weighted Max-Cut using QAOA. Confirm the official problem code, graph instance, and metric definitions against the Challenge Kit before submission.

## Methodology
Use the same logical problem instance, QAOA depth, parameter-selection procedure, shot count, and random-seed policy for both processor models. Compile separately against each coupling map and record circuit depth, two-qubit gate count, SWAP count, and objective-value statistics.

## Processor definitions
- **Processor A:** five-qubit graph transcribed from the organizer reference image; illustrative noise only.
- **Processor B:** current seven-qubit coupling map is provisional because the reference image's visible node count conflicts with its label. Do not claim it is the official model until confirmed.

## Results
Populate this section only from a clean execution of `main.ipynb`. Clearly distinguish ideal simulation, simulated noise, and actual hardware results. Do not describe simulated results as hardware measurements.

## Interpretation
Compare measured problem performance and compilation/resource metrics. Attribute differences to architecture only when the experiment controls other factors; state remaining uncertainties.

## Limitations
The current Processor B graph and noise parameters are assumptions. The working Max-Cut graph is a team-defined test instance. Replace these with organizer-supplied specifications where applicable before final submission.

## AI assistance
AI tools were used to assist with project scaffolding and code drafting. Team members must verify, understand, test, and take responsibility for the final implementation, and adapt this disclosure to the event's policy.
