# ML workspace

A uv workspace with two packages:

- **`algorithm/`**: toy optimisation algorithm (random sampler here). Packaged
  into a container (see `Dockerfile`) to demonstrate how an ML workspace
  member becomes a deployable artefact. Not wired to Django in this template
  - adapt to your runtime of choice (Batch, ECS, Cloud Run, K8s job, ...).
- **`evaluation/`**: offline pipeline for evaluating the algorithm. Never
  deployed. Placeholder in this template only to show that the
  workspace can host more than one member, each with its own deployment
  story.

Run `just setup` (from this folder or via `just backend ml setup` from the
repo root) to sync the workspace and build the algorithm image.
