# Wire the api module up for the staging environment.

module "api" {
  source       = "../../modules/api"
  name         = "api-staging"
  image        = "ghcr.io/your-org/api:staging"
  database_url = "postgres://example"
}

output "api_url" {
  value = module.api.url
}
