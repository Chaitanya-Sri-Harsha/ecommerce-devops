pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone') {
            steps {
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/master']], // change to '*/master' if that's your default
                          userRemoteConfigs: [[url: 'https://github.com/Chaitanya-Sri-Harsha/ecommerce-devops.git']]
                ])
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
