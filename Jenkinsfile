pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                deleteDir() // cleans the workspace
            }
        }

        stage('Clone') {
            steps {
                git 'https://github.com/Chaitanya-Sri-Harsha/ecommerce-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("ecommerce-app")
                }
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 ecommerce-app'
            }
        }
    }
}
