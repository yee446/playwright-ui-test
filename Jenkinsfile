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
                // 使用完整的 Python 路径
                bat '"C:\\Users\\yee\\Downloads\\python.exe" -m venv venv'
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\Downloads\\Scripts\\pip.exe" install -r requirements.txt'
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\Downloads\\Scripts\\playwright.exe" install'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\Activate.ps1 && "C:\\Users\\yee\\Downloads\\Scripts\\pytest.exe" tests/ --html=reports/report.html --self-contained-html'
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
