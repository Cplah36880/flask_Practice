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
            echo "===== Deploy Stage ====="

            rm -rf deployment
            mkdir deployment

            cp app.py deployment/
            cp requirements.txt deployment/
            cp -r templates deployment/

            echo "Deployment completed successfully."
            ls -R deployment
        '''
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
