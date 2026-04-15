pipeline {
    agent any
    stages {
        stage('执行测试') {
            steps {
                bat '''
                    @echo off
                    chcp 65001
                    pytest
                '''
            }
        }
    }
}
