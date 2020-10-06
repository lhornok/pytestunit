pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Tests..'
                dir ('tests'){
                  sh '/usr/bin/py.test-3 --junitxml results.xml foxtests.py'
                }
            }
        }
    }
}
