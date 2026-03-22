pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Clone Code') {
            steps {
                git 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t mlops-project .'
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    sh 'docker rm -f mlops-container || true'
                }
            }
        }

        stage('Run Container') {
            steps {
                script {
                    sh 'docker run -d -p 8000:8000 --name mlops-container mlops-project'
                }
            }
        }
    }
}