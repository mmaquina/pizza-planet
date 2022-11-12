## Set up your working environment
### You need
* AWS account credentials
* The latest version of the AWS Command Line Interface (AWS CLI). 
* Terraform14.7+
* Docker Desktop 3.1.0+ 
* Boto3 installed on local workstation.

## Config
Perform local configuration. You can start following the next link (not to the letter)
https://aws.amazon.com/blogs/opensource/automate-python-flask-deployment-to-the-aws-cloud/

Perform AWS config, by CLI or the graphical interface (or both).



Create the .github/file.yaml to trigger the deployment whenever a new release is created. That would be for the production environment. If we are creating a "stage" deployment for testing, we could trigger the pipeline on merges to main branch. 

## Test the pipeline
Create an event to trigger the CD pipeline.

## Acceptance criteria
* Pipeline runs are correctly displayed in AWS console and in GitHub actions
* The desired version of the app is online after a new release is made
