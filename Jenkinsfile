pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:3.11.5-alpine3.18' 
                }
            }
            steps {
                sh 'python -m py_compile add2vals.py calc.py' 
                stash(name: 'compiled-results', includes: '*.py*') 
            }
        }
    }
}