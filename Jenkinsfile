pipeline {
    agent any
    environment {
        PYTHONIOENCODING = 'UTF-8'
    }
    stages {
        stage('拉取代码') {
            steps {
                git branch: 'main', url: 'https://github.com/yee446/playwright-ui-test.git'
            }
        }
        stage('安装依赖') {
            steps {
                bat '''
                    @echo off
                    chcp 65001
                    "C:\\Python311\\python.exe" -m pip install --upgrade pip
                    "C:\\Python311\\python.exe" -m pip install -r requirements.txt
                    "C:\\Python311\\python.exe" -m playwright install chrome
                '''
            }
        }
        stage('执行测试') {
            steps {
                bat '''
                    @echo off
                    chcp 65001
                    "C:\\Python311\\python.exe" -m pytest --alluredir=report/xml
                '''
            }
        }
    }
    post {
        always {
            allure results: [[path: 'report/xml']]
        }
    }
}
