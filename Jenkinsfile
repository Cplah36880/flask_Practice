pipeline {
    agent any

    environment {
        PIP_BREAK_SYSTEM_PACKAGES = "1"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    python3 --version

                    python3 -m pip install --upgrade pip --break-system-packages

                    python3 -m pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    python3 -m pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p deployment
                    cp -r * deployment/
                    echo "Deployment Successful"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }

        always {
            cleanWs()
        }
    }
}
