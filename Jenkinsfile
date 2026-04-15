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
        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m pytest test_demo.py -v'
            }
        }
    }
}
