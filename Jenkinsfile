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
                // 使用 Python 39 的绝对路径
                bat '"C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pip.exe" install -r requirements.txt'
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\playwright.exe" install'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pytest.exe" tests/ --html=reports/report.html --self-contained-html'
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
