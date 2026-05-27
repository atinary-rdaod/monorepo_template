# Skeleton module for the API service. Replace the body with the resources
# your provider exposes (ECS, Cloud Run, Kubernetes, fly.io, …). Inputs and
# outputs below capture the contract we found useful at the talk's source
# company.

variable "name" {
  description = "Service name, used as a prefix for every resource."
  type        = string
}

variable "image" {
  description = "Container image (e.g. ghcr.io/your-org/api:1.2.3)."
  type        = string
}

variable "database_url" {
  description = "Connection string for the API's Postgres database."
  type        = string
  sensitive   = true
}

output "url" {
  description = "Public URL of the deployed API."
  value       = "https://${var.name}.example.com"
}
