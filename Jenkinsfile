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
                    sh 'pip install -r src/requirements.txt'
                    sh 'pip list > abcd'
                    sh 'sudo apt-get install binutils'
                    sh 'pyinstaller -y --clean --name dot_local_api --additional-hooks-dir ./src/extra-hooks ./src/main.py --onefile'
                    sh 'ls -l > abcd'
                    stash(name: 'compiled-results', includes: 'src/*.py*')
            }
            post {
                success {
                    archiveArtifacts "dist/dot_local_api"
                    archiveArtifacts "abcd"
                }
            }
        }

    }
}