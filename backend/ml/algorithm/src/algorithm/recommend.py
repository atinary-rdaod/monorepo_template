import numpy as np

from algorithm.models import Experiment, Recommendation, Run


def recommend(experiment: Experiment) -> Run:
    """Random-sample the decision space — the toy algorithm shipped by this
    template. Replace the body with your real model."""
    rng = np.random.default_rng()
    recommendations = [
        Recommendation(values={p.name: float(rng.uniform(p.lower, p.upper)) for p in experiment.parameters})
        for _ in range(experiment.batch_size)
    ]
    return Run(run_id="", recommendations=recommendations)
