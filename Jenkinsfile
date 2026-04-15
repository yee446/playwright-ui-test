pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
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
