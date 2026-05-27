# infrastructure

Infrastructure-as-code lives here. The talk's source company uses OpenTofu —
this template includes a single example module to show the layout without
prescribing a cloud.

```
infrastructure/
├── README.md
├── modules/              # reusable modules
│   └── api/              # example: container service + DB
└── environments/
    ├── staging/
    └── production/
```

Pick your tool of choice (Terraform, OpenTofu, Pulumi, CDK, …) — what matters
is that it lives in the same repo as the code it deploys, owned via
`.github/CODEOWNERS`.
