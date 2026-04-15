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
                // 创建虚拟环境
                bat 'if not exist venv ( "C:\\Users\\yee\\AppData\\Local\\Programs\\Python\\Python39\\python.exe" -m venv venv )'
                
                // 直接安装依赖，不读 requirements.txt（解决报错！）
                bat 'call venv\\Scripts\\activate.bat && pip install pytest playwright'
                
                // 安装浏览器
                bat 'call venv\\Scripts\\activate.bat && playwright install chromium'
            }
        }
        
        stage('Run Tests') {
            steps {
                bat 'call venv\\Scripts\\activate.bat && pytest'
            }
        }
    }
    
    post {
        always {
            echo '构建完成！'
        }
    }
}
