from algorithm import Experiment, Parameter, recommend


def test_recommend_respects_batch_size_and_bounds() -> None:
    experiment = Experiment(
        id="exp",
        parameters=[Parameter(name="x", lower=0.0, upper=1.0)],
        batch_size=3,
    )
    run = recommend(experiment)

    assert len(run.recommendations) == 3
    for rec in run.recommendations:
        assert 0.0 <= rec.values["x"] <= 1.0
