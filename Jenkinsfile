pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\Activate.ps1 && pip install -r requirements.txt'
                bat 'venv\\Scripts\\Activate.ps1 && playwright install'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\Activate.ps1 && pytest tests/ --html=reports/report.html --self-contained-html'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
            junit 'reports/junit-results.xml'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}