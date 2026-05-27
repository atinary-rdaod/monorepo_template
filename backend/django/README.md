# django

Django monolith. The whole product fits in a single project; new domains are
added as new `apps/<name>/` modules. The structure follows
[HackSoft's Django styleguide](https://github.com/HackSoftware/Django-Styleguide):

- `apps/<name>/api.py`        — DRF views.
- `apps/<name>/selector.py`   — read functions (queries).
- `apps/<name>/service.py`    — write functions (commands).
- `apps/<name>/serializers/`  — request/response shapes.
- `apps/<name>/models/`       — Django models.
- `apps/<name>/tasks/`        — Celery tasks.

## Run it

```bash
just setup        # copy .env, sync uv, bring docker stack up, migrate
just run          # apply migrations + runserver
```

`just run` (from this folder) is also the recipe wired into the root justfile
as `just backend run`.
