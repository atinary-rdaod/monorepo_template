module "api" {
  source       = "../../modules/api"
  name         = "api-production"
  image        = "ghcr.io/your-org/api:latest"
  database_url = "postgres://example"
}
