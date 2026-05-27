mod backend

@_:
  just --list

# Bootstrap the entire monorepo (backend, frontend, pre-commit).
setup:
    just backend::setup
    just frontend_setup
    uv tool run pre-commit install

# Run the frontend dev server.
[working-directory: "frontend"]
run:
    npm run dev

[working-directory: "frontend"]
frontend_setup:
    npm install

# Regenerate TypeScript types from the backend OpenAPI schema.
generate_types:
    just backend django _generate_openapi_schema
    cd frontend && npm run openapi

# Run pre-commit hooks across the repo.
pre_commit:
    uv tool run pre-commit run --all-files
