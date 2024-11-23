pipeline {
    agent any

    environment {
        IMAGE_NAME = 'web-app'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout Code') {
            steps { 
                git url: 'https://github.com/ShivamD26/CVAssignment_MITAOE.git/', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                script {
                    bat "docker run --rm -d -p 8501:8501 --name test-container ${IMAGE_NAME}:${IMAGE_TAG}"
                    retry(5) {
                        bat "curl -f http://localhost:8501"   
                        sleep 2  
                    }
                    bat "docker stop test-container"
                }
            }
        }

        stage('Push to Registry') {
            steps {
                script { 
                    withDockerRegistry([credentialsId: 'ab1ef886-b666-4d72-ab62-d9c62c80b1aa']) { 
                        bat "docker push shivd26/cloud-prac:latest"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
