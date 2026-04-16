pipeline {
    agent any

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
