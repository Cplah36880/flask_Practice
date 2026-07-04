pipeline {
    agent any

    environment {
        MONGO_URI = "mongodb://localhost:27017/test_student_db"
        SECRET_KEY = "jenkins-secret"
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
                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest test_app.py -v
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    mkdir -p deployment
                    cp -r * deployment/
                    echo "Deployment completed successfully."
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
