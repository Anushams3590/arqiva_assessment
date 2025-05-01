output "api_url" {
  description = "Dynamic string display html url"
  value       = "${aws_api_gateway_deployment.deployment.invoke_url}/html"
}