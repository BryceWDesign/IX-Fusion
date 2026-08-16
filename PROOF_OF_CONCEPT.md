# IX-Fusion Proof of Concept

Release 0.1 tests the C6-derived seed against a matched five-field-period helical control
using the repository's dimensionless reduced-order model and equal optimizer budget.

## Verdict

**`FAIL_OR_INCONCLUSIVE`**

Scientific stage remains **`geometry_hypothesis`**.

## Why the result is not simply "bad"

The C6 candidate produces a **28.65% lower mean radial-excursion proxy** than the matched
control in the internal field-line screen. That is the most interesting favorable signal in
release 0.1.

However, the candidate also has:

- a **4.87% worse** composite screening objective;
- a **0.17% worse** bounce-action variation proxy;
- a **10.47% higher** engineering burden proxy, narrowly exceeding the predeclared 10%
  allowance;
- the same zero escape fraction in the tested reduced field-line set.

Because the project uses multiple independent gates, the favorable radial-excursion result
does not override the other failures.

## Additional evidence

The six-source phased-actuator signal model shows that abstract feedback increases median
target spatial-mode purity from approximately **99.21% to 99.93%** under the committed
error assumptions, corresponding to an approximately **11.05x** reduction in median
unwanted-mode power in that signal model.

This is not evidence of RF heating or plasma control. It only verifies the control-layer
mathematics under the declared abstract assumptions.

The geometry-error Monte Carlo also shows a mixed result: the C6 candidate has slightly
lower median relative degradation than the matched baseline under the committed parameter
perturbation distribution, but the candidate begins from a worse nominal composite score.

## Important model warning

The no-axis-helical-shaping ablation improves the internal composite objective. That is not
a physical recommendation. It exposes a known limitation: rotational transform is
parameterized in the reduced model instead of being derived self-consistently from 3-D
coils/equilibrium. The result is retained as a falsification signal showing why a proper
MHD/coil solver is mandatory before any stronger claim.

## Next decision

Do not tune the internal model until C6 "wins." The next scientifically meaningful step is
to integrate a solved equilibrium/coil pipeline and retest the same hypothesis against fair
controls.

Exact evidence: `results/poc/POC_RESULT.md`, `results/poc/verdict.json`, and
`results/evidence/IXFUSION-POC-001.json`.
