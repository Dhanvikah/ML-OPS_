pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t mlops-project .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f mlops-container || true'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 8001:8000 --name mlops-container mlops-project'
            }
        }
    }
}