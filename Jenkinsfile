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
                bat '''
                    @"C:\Users\yee\AppData\Local\Programs\Python\Python39\python.exe" -m pip install -r requirements.txt
                    @"C:\Users\yee\AppData\Local\Programs\Python\Python39\python.exe" -m playwright install chromium
                '''
            }
        }
        stage('Run All Tests') {
            steps {
                // 关键：执行 tests/ 目录下所有用例 + 根目录用例，生成完整报告
                bat '"C:\Users\yee\AppData\Local\Programs\Python\Python39\python.exe" -m pytest tests/ . -v --html=reports/report.html --self-contained-html'
            }
        }
    }
    post {
        always {
            // 归档报告，在 Jenkins 直接查看
            archiveArtifacts artifacts: 'reports/**', fingerprint: true
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'UI自动化测试全量报告'
            ])
        }
    }
}
