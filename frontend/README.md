# frontend

Tiny Vite + React + TypeScript SPA. The structure mirrors the talk's source
codebase: API types are **generated** from the OpenAPI schema produced by
the Django backend, written to `src/generated/`. Both the schema and the
generated types are gitignored — `just setup` (or `just generate_types`)
regenerates them.

## Commands

```bash
npm install         # install (or `npm ci` once package-lock.json is committed)
npm run openapi     # regenerate types from ../generated/openapi-schema.yml
npm run dev         # Vite dev server on :5173
npm run build       # production build
npm run typecheck   # tsc -b
```

`just run` from the repo root is a shortcut for `npm run dev`.
