pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/PranitMaldikar/Portfolio-Test-Automator'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                withCredentials([
                    string(credentialsId: 'USER_NAME', variable: 'USER_NAME'),
                    string(credentialsId: 'PASSWORD', variable: 'PASSWORD'),
                    string(credentialsId: 'DASHBOARD_URL', variable: 'DASHBOARD_URL')
                ]) {
                    sh 'export USER_NAME=$USER_NAME'
                    sh 'export PASSWORD=$PASSWORD'
                    sh 'export DASHBOARD_URL=$DASHBOARD_URL'
                    sh 'browserstack-sdk behave features/stockTransaction.feature'
                }
            }
        }
    }
}
