import json
import boto3
import os

def lambda_handler(event, context):
    # Initialize SSM client
    ssm_client = boto3.client('ssm')
    
    # Get project name from environment variable
    project_name = os.environ['PROJECT_NAME']
    
    # Fetch the dynamic string from Parameter Store
    parameter_name = f"/{project_name}/dynamic-string"
    try:
        response = ssm_client.get_parameter(Name=parameter_name)
        dynamic_string = response['Parameter']['Value']
    except Exception as e:
        dynamic_string = "Error fetching string"
    
    # Generate HTML content
    html_content = f"<h1>The saved string is {dynamic_string}</h1>"
    
    # Return HTTP response
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "text/html"
        },
        "body": html_content
    }