# Flask-HelloWorld
Simple Dockerized Flask Project that shows 'Hello World" through a JSON message. The project also, using a Shell Script file, is deployed to the Azure cloud through a container instance created with Azure CLI.
Finally, we created a GitHub Actions Workflow for the project which consists of a configurable automated process composed of one or more jobs.

## Installation and Deployment
* Install Docker using the official documentation in [```Docker/Install```](https://docs.docker.com/engine/install/ubuntu/)
* Install Azure CLI following the correct instructions according to the current used OS in [```Azure CLI/Install```](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* Install Docker image using ```docker build -t flask_project:v1.0.0 .```
* Execute container to try it out locally with ```docker compose up```
* Once the container has run successfully, you can deploy it to the cloud with ```./deploy.sh```
## GitHub Actions
You can build and deploy the application to Azure Cloud using GitHub Actions using an YML File.
### Steps
* Go to ```Settings\Security\Secrets and variables\Actions```
* In the Secrets section, select ```new repository secret``` and set each secret variable with its specific value.
* Once you have setted all the secret variables, you need to go to the Actions section and run the workflow.
### Azure Credentials for deployment
To get the Azure credentials, you need to enter the following command:
```bash
az ad sp create-for-rbac --name service_principal_name --role contributor --scopes /subscriptions/id_suscription --sdk-auth
```
The previous command provides a JSON with the Azure secret credentials.

Note: These credentials are no longer available for review, so it is recommended to copy and save them as a secret variable in the remote GitHub repository. 
## Pushing Tag with Actions
In order to build and deploy with a tag version in our GitHub Actions Workflow, we need to push first the specific tag version of the project.
```bash
git tag v*.*.* # specific tag version
```
```bash
git push origin v*.*.*
```
After pushing it, we simply have to go to the Actions section and re-run the workflow.
## Security
We use Snyk tool to check the workflow security. To achieve this, we use Snyk Token as an Actions Variable.
To add your token to your variables, you need to do the following steps:
* Go to [```Snyk-App```](https://app.snyk.io/)
* Search for ```Account\Settings\General\Auth\```
* Click on ```click to show``` to reveal the Snyk Token.
* Go to Actions and add it.
## Tools
![ShellScript](https://img.shields.io/badge/Shell_Script-43853D?style=for-the-badge&logo=gnu-bash&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white) ![GithubActions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
