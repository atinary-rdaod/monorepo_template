from pydantic import BaseModel, Field


class Parameter(BaseModel):
    name: str
    lower: float
    upper: float


class Experiment(BaseModel):
    id: str
    parameters: list[Parameter]
    batch_size: int = Field(default=1, ge=1)


class Recommendation(BaseModel):
    values: dict[str, float]


class Run(BaseModel):
    """Wire format exchanged between the algorithm and the Django API."""

    run_id: str
    recommendations: list[Recommendation]
