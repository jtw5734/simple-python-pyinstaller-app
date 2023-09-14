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
                    sh 'pip install -r src/requirements.txt'
                    sh 'pip list > abcd'
                    sh 'cd src'
                    sh 'make onefile'
                    stash(name: 'compiled-results', includes: 'src/*.py*')
            }
            post {
                success {
                    archiveArtifacts "dist/dot_local_api"
                }
            }
        }

    }
}