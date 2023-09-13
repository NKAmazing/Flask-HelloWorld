# Flask-HelloWorld
Simple Dockerized Flask Project that shows 'Hello World" through a JSON message. The project also, using a Shell Script file, is deployed to the Azure cloud through a container instance created with Azure CLI.
Finally, we created a GitHub Actions Workflow for the project which consists of a configurable automated process composed of one or more jobs.

## Instalation and Deployment
* Install Docker using the official documentation in [```Docker/Install```](https://docs.docker.com/engine/install/ubuntu/)
* Install Azure CLI following the correct instructions according to the current used OS in [```Azure CLI/Install```](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* Install Docker image using ```docker build -t flask_project:v1.0.0 .```
* Execute container to try it out locally with ```docker compose up```
* Once the container has run successfully, you can deploy it to the cloud with ```./deploy.sh```
## Tools
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white) ![GithubActions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)
