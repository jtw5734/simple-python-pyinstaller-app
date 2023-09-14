pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.11.5-alpine3.18'
                    args '-u root --privileged'
                }
            }
            steps {
                    sh 'python -m venv ./venv'
                    sh 'source venv/bin/activate'
                    sh 'pip install -r sources/requirements.txt'
                    sh 'pip list > abcd'
                    sh 'python sources/main.py'
                    stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
            post {
                success {
                    archiveArtifacts "abcd"
                }
            }
        }

    }
}