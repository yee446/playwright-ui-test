pipeline {
    agent any
    tools {
        python 'Python' // 关键：让 Jenkins 识别系统 Python
    }
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
                    py -m pip install --upgrade pip
                    py -m pip install -r requirements.txt
                    py -m playwright install chrome
                    py -m playwright install-deps
                '''
            }
        }
        stage('执行测试') {
            steps {
                bat '''
                    py -m pytest --alluredir=report/xml
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
