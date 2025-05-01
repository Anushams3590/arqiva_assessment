## ARQIVA test assessment
This repository contains test assignment for arqiva.

## Usage
Pre-requisite tools: python3.10, terraform1.11.3, AWS Lambda, AWS Systems Manager Parameter Store

### Repo Directory Structure
Files are organised in my folder structure in the Repository

|---- arqiva_assessment
|	|——  main.tf
|	|—— variables.tf
|	|—— outputs.tf
|	|—— lambda_function.py
|	|—— README.md


### Steps to execute 

 >> terraform init
 >> terraform plan
 >> terraform apply

—> To access the web page in your browser, click on the link from terraform output:
	Eg: 
	   Outputs:
	   >> api_url = "https://zaf1g35qfe.execute-api.eu-west-2.amazonaws.com/prod/html"

—> To change string value in ssm store
>>  aws ssm put-parameter --name "/dynamic-string-value/dynamic-string" --value "NewDynamicString" --type String --overwrite --region eu-west-2

### How It Works

   —> `main.tf` - contains the infrastructure, Lambda, API Gateway, and Parameter Store.
   —>`variables.tf` -  customization of the region, project name, and initial string.
   —> `outputs.tf` -  provides the API Gateway URL.
   —> `lambda_function.py` - contains the Lambda code that fetches the string from Parameter Store and returns the HTML.
   —> The string is stored in Parameter Store under `/dynamic-string-value/dynamic-string`.
   —> The Lambda function retrieves the string on each request, ensuring consistency across users.
   
### Architectural factors

Choosen solution:
AWS Lambda + Parameter Store
	This solution provides a simple, scalable, and cost-effective way to serve a dynamic HTML page on AWS using a serverless architecture. The use of Lambda, 	API Gateway, and Parameter Store meets the requirements for dynamic updates and consistency, while Terraform ensures the infrastructure is reproducible 		and manageable. 

  Pros:
	- Serverless Architecture, auto-scaling, cost-effective for low traffic.
	- Parameter Store provides seamless updates to the dynamic string.
	- AWS is widely used, has a mature serverless ecosystem, and offers Parameter Store for dynamic configuration management.

	Cons:
	- Lambda can produce latency due to cold starts.
	- API Gateway Costs - Per-request pricing can add up for high traffic (S3 static hosting might be cheaper)

Potential embellishments with more time:
	- IAM roles can introduced to follow the principle of least privilege and S3 bucket for state is encrypted.
	- Adding a custom domain using Route53
	- Add CSS and JavaScript to the HTML page for better presentation and interactivity


### Other solutions

AWS EC2 + Parameter store + Django application
 
   - Deploy a small Django application on EC2 to serve the HTML.
   - Use SSM to store the string.
   - Pros: More control over the server, changing the string in SSM dynamically updates the Django app, no redeployment needed, allow public HTTP access through 	a Security Group.
   - Cons: Requires server management, higher cost, and more complex updates.



