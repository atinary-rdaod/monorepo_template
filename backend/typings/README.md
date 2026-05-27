# Shared type stubs

This folder holds [PEP 561](https://peps.python.org/pep-0561/) stub packages
for third-party libraries whose published types are missing, incomplete, or
incorrect. The `stubPath` is set once in `backend/pyproject.toml` under
`[tool.basedpyright]`, so a stub written here is reused by every Python
project in the monorepo.

To add a stub for a library called `foo`:

1. Create `typings/foo/__init__.pyi` (and any submodules you need).
2. Drop in just the symbols you actually call — partial stubs are fine.
3. Re-run `just backend type` to verify pyright picks the stubs up.

Keep stubs lean: every annotation you add here you also have to maintain.
