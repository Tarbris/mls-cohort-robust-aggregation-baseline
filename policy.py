"""Editable federated aggregation strategy; weak sample-size weighting."""


class Strategy:
    def aggregate(self, updates):
        total = sum(u["n"] for u in updates)
        dimension = len(updates[0]["delta"])
        return [sum(u["n"] * u["delta"][j] for u in updates) / total for j in range(dimension)]
