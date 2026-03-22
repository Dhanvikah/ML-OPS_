pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t mlops-project .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f mlops-container || exit 0'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 8000:8000 --name mlops-container mlops-project'
            }
        }
    }
}