pipeline {
    agent any
    environment {
        PYTHONIOENCODING = 'UTF-8'
    }
    stages {
        stage('安装依赖') {
            steps {
                echo '>>> 开始安装项目依赖'
                bat '''
                    @echo off
                    chcp 65001
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                    python -m playwright install chrome
                    python -m playwright install-deps
                '''
            }
        }
        stage('执行自动化测试') {
            steps {
                echo '>>> 开始执行 UI 自动化测试'
                bat '''
                    @echo off
                    chcp 65001
                    python -m pytest --alluredir=./report/xml --junitxml=./report/junit.xml
                '''
            }
            post {
                always {
                    allure(
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'report/xml']]
                    )
                    junit 'report/junit.xml'
                }
            }
        }
    }
    post {
        always {
            echo '>>> 流水线执行完成！'
        }
    }
}
