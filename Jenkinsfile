pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Tests..'
                sh '/usr/bin/py.test-3 --junitxml results.xml foxtests.py'
            }
        }
    }
    post {
        always {
            junit 'results.xml'
        }
    }
}
