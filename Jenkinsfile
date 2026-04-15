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
                // 只在虚拟环境不存在时创建
                bat 'if not exist venv ( "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m venv venv )'
                
                // 安装依赖（关键修复：用 activate.bat）
                bat 'call venv\\Scripts\\activate.bat && "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\pip.exe" install -r requirements.txt'
                
                // 安装浏览器
                bat 'call venv\\Scripts\\activate.bat && "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\playwright.exe" install --with-deps chromium'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && pytest tests/ --html=reports/report.html --self-contained-html'
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
