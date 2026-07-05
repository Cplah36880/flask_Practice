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
                    echo "===== Python Version ====="
                    python3 --version

                    echo "===== Pip Version ====="
                    python3 -m pip --version

                    echo "===== Installing Dependencies ====="
                    python3 -m pip install --upgrade pip --break-system-packages
                    python3 -m pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    echo "===== Running Tests ====="
                    pytest -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    echo "===== Deploy Stage ====="
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
