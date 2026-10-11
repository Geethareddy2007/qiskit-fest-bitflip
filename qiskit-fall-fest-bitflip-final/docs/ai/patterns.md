# Engineering Patterns — Team BitFlip

## Configuration-driven processor definitions
Keep processor properties in JSON and load them through shared code to reduce duplicated configuration.

## Separate problem and processor logic
Keep Max-Cut graph/scoring logic separate from processor configuration and circuit evaluation where the project structure supports it.

## Validate quantum results against a classical reference
Compare sampled QAOA cuts with the exact optimum for the same graph. Report the objective and how it was obtained.

## Make assumptions explicit
Distinguish official hardware facts from team working models. Processor B's 9-qubit chain is provisional; noise values are illustrative.

## Reproducibility checklist
- Record package versions.
- Record graph edges and weights.
- Record QAOA depth, optimizer, shots, seeds, and stopping criteria.
- Save results and plots with clear filenames.
- Separate observations from interpretations.
