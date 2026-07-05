# Flask Practice CI/CD Project

## Project Overview

This project demonstrates a complete CI/CD implementation for a Flask web application using Jenkins and GitHub Actions.

---

## Technologies Used

- Python
- Flask
- Jenkins
- GitHub Actions
- Git
- PyTest

---

## Jenkins CI/CD Pipeline

The Jenkins pipeline consists of the following stages:

1. Checkout Source Code
2. Build
3. Test
4. Deploy

### Build

Installs all project dependencies using:

```
pip install -r requirements.txt
```

### Test

Runs the test suite using:

```
pytest
```

### Deploy

Copies the application files into the deployment folder after successful testing.

---

## GitHub Actions Workflow

The GitHub Actions workflow automatically performs:

- Checkout Repository
- Install Dependencies
- Run Tests
- Build Application
- Deploy to Staging (staging branch)
- Deploy to Production (release)

---

## GitHub Secrets

The following repository secrets are configured:

- DEPLOY_KEY
- API_TOKEN

---

## Branches

- main
- staging

---

## Prerequisites

- Python 3
- Git
- Jenkins
- GitHub Account

---

## Repository Structure

```
.
├── app.py
├── Jenkinsfile
├── requirements.txt
├── test_app.py
├── templates/
└── .github/workflows/ci.yml
```

---

## Repository

GitHub Repository:

https://github.com/Cplah36880/flask_Practice

---

## Author

Submitted as part of the HeroVired DevOps Assignment.
