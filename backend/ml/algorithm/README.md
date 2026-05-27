# algorithm

Pure-Python library exposing `recommend(experiment) -> Run`. The body is a
one-liner random sampler — the structure is the point. Replace
`recommend.py` with your real model.

The accompanying `../Dockerfile` builds this package into a container image
to demonstrate the packaging pattern, but the template doesn't wire that
container to anything: bring your own runtime (AWS Batch, ECS, Cloud Run,
Kubernetes job, ...) and call `recommend_to_<your-api>` however you like.
