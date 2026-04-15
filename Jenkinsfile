pipeline {
    agent any
    environment {
        // 统一编码，避免中文乱码
        PYTHONIOENCODING = 'UTF-8'
    }
    stages {
        stage('拉取代码') {
            steps {
                echo '>>> 开始拉取 GitHub 最新代码'
                git branch: 'main', url: 'https://github.com/yee446/playwright-ui-test.git'
            }
        }
        stage('安装依赖') {
            steps {
                echo '>>> 开始安装项目依赖'
                bat '''
                    @echo off
                    chcp 65001
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install chrome
                    playwright install-deps
                '''
            }
        }
        stage('执行自动化测试') {
            steps {
                echo '>>> 开始执行 UI 自动化测试'
                bat '''
                    @echo off
                    chcp 65001
                    pytest --alluredir=./report/xml --junitxml=./report/junit.xml
                '''
            }
            post {
                always {
                    echo '>>> 生成 Allure 测试报告'
                    allure(
                        includeProperties: false,
                        jdk: '',
                        results: [[path: 'report/xml']]
                    )
                    // 生成 JUnit 测试结果统计
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
