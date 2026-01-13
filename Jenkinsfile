pipeline {
    agent any
     environment {
        VIRTUAL_ENV = "/var/jenkins_home/venv"
        PATH = "${VIRTUAL_ENV}/bin:${env.PATH}"
        PYTHONPATH = "${WORKSPACE}"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 --version
                    pip3 install -r requirements.txt
                 '''
            }
        }
        stage('Run Playwright Tests') {
            steps {
                sh '''
                    pytest tests --html=report.html
                '''
            }
        }
    }
    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright Test Report'
            ])
        }
        failure {
            echo 'Tests failed'
        }
        success {
            echo 'Tests passed'
        }
    }
}
