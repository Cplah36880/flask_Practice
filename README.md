# Flask CI/CD Project using Jenkins

## Objective

This project demonstrates a CI/CD pipeline for a Flask application using Jenkins.

## Prerequisites

- Jenkins
- Python 3
- Git
- GitHub
- Flask

## Repository

https://github.com/Cplah36880/flask_Practice

## Pipeline Stages

### Checkout

Downloads the latest source code from GitHub.

### Build

Installs all dependencies from requirements.txt.

### Test

Runs unit tests using pytest.

### Deploy

Copies the application files into the deployment directory.

## Trigger

The pipeline can be triggered manually or automatically using GitHub Webhooks.

## Notifications

Email notifications can be configured in Jenkins.

## Deployment

Deployment creates a deployment folder containing:

- app.py
- templates/
- requirements.txt
- README.md

## Author

Your Name
