pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh('script.sh')
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
