# Cohort-aware robust federated aggregation

Edit `policy.py` only. Implement `Strategy.aggregate(updates)`; each update is
`{"cohort": 0|1, "n": positive integer, "delta": list[8 floats]}`. Return
eight finite floats. One call represents a communication round. The cohort
IDs are operational strata and are public. Client sample counts are provided
but may be uneven; update vectors may include a minority of arbitrary values.

The intended server update is the equally weighted mean of the two honest
cohort centers, rather than a sample-size-weighted mean of all received
messages. Each round has 10 clients per cohort, of which at most two per
cohort may send arbitrary updates. The identities of those clients and the
honest centers are unknown. Rounds use fresh client messages and target
vectors. Development instances include target vectors for tuning; hidden
targets and evaluator reference files must not enter the solver process.
