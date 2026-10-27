# Cohort-aware robust federated aggregation

Edit `policy.py` only. Implement `Strategy.aggregate(updates)`; each update is
`{"cohort": 0|1, "n": positive integer, "delta": list[8 floats]}`. Return
eight finite floats representing a server gradient. One call represents a
communication round; a single Strategy object persists across 18 rounds.
The evaluator starts the global model at the eight-dimensional zero vector
and updates `model = model - 0.55 * aggregate(updates)` after each call. Honest
client deltas are noisy gradients of local quadratic objectives at the
current model; the two cohorts have different local optima. Cohort IDs are
public. Client sample counts may be uneven and a minority of updates arbitrary.

The target global objective is the equally weighted average of the two
honest cohort quadratic objectives, not a sample-size-weighted objective.
Each round has 10 clients per cohort, of which at most two per cohort may
send arbitrary updates. Their identities, the honest local optima and the
global optimum are unknown. Rounds use fresh client messages; the returned
gradient changes the next round's observed updates. Development instances
include the optimum and all round specifications for tuning; hidden targets
and evaluator reference files must not enter the solver process.
