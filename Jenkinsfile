pipeline {
    agent any

    environment {
        XRAY_CLIENT_ID = credentials('XRAY_CLIENT_ID')
        XRAY_CLIENT_SECRET = credentials('XRAY_CLIENT_SECRET')
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests & Upload to Xray') {
            steps {
                bat 'python run_tests.py'
            }
        }
    }
}