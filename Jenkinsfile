pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/tanwar1d/xray-python-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python run_tests.py'
            }
        }
    }
}