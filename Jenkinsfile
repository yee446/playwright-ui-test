pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
<<<<<<< HEAD
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
=======
        stage('Run Tests') {
            steps {
                bat '''
                    @echo off
                    chcp 65001
                    "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest
                '''
            }
        }
    }
}
>>>>>>> 25c4041eadb96bf23ba908853e5a89ed4767a2b7
