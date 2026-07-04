pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                python3 -m pip install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                pytest test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                mkdir -p deployment
                cp -r * deployment/
                echo "Application deployed to staging successfully."
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed!'
        }
        always {
            cleanWs()
        }
    }
}
