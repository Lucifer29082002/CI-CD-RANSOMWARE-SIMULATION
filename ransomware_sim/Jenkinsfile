pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'ransomware-sim'
        CONTAINER_NAME = 'ransomware-test'
    }

    stages {

        // Stage to checkout code from the GitHub repository
        stage('Checkout Code') {
            steps {
                // Checkout the repository with the Jenkinsfile from GitHub
                git branch: 'main', url: 'https://github.com/Lucifer29082002/CI-CD-RANSOMWARE-SIMULATION.git'
            }
        }

        // Stage to build the Docker image
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        // Stage to run the Docker container
        stage('Run Simulation Container') {
            steps {
                echo 'Running the Docker container...'
                sh 'docker run -d --rm --name $CONTAINER_NAME $DOCKER_IMAGE'
            }
        }

        // Stage to verify encryption (check the contents of a file within the container)
        stage('Verify Encryption') {
            steps {
                echo 'Verifying encryption on sample file...'
                sh 'docker exec $CONTAINER_NAME cat target_files/sample1.txt || true'
            }
        }

        // Stage to stop the Docker container after the tests
        stage('Stop Container') {
            steps {
                echo 'Stopping the Docker container...'
                sh 'docker stop $CONTAINER_NAME || true'
            }
        }
    }

    post {
        always {
            // Clean up any remaining Docker containers
            echo 'Cleaning up...'
            sh 'docker stop $CONTAINER_NAME || true'
        }
    }
}
