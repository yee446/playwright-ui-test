pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m playwright install chromium'
            }
        }
        stage('Run All Tests') {
            steps {
                bat '"C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest tests/ test_demo.py -v --html=reports/report.html'
            }
        }
    }
}
