# 更新 Jenkinsfile
$jenkins_content = @'
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
                bat 'if not exist venv ( "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m venv venv )'
                bat 'venv\\Scripts\\Activate.ps1 && pip install -r requirements.txt'
                bat 'venv\\Scripts\\Activate.ps1 && playwright install'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\Activate.ps1 && pytest tests/test_baidu_search.py --html=reports/report.html'
            }
        }
    }
}
'@
Set-Content "c:\Users\yee\Documents\trae_projects\play\Jenkinsfile" $jenkins_content
