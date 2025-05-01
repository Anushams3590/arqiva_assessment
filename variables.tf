variable "region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "eu-west-2"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "dynamic-string-value"
}

variable "initial_dynamic_string" {
  description = "Initial value for the dynamic string"
  type        = string
  default     = "HelloWorld"
}