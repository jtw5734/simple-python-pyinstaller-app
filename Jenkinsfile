pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root --privileged'
                }
            }
            steps {
                    sh 'apt-get install binutils'
                    sh 'ls -l > abcd'
                    sh 'pip install -r src/requirements.txt'
                    sh 'pip list > abcd'
                    sh 'pyinstaller -y --clean --name dot_local_api --additional-hooks-dir ./src/extra-hooks ./src/main.py --onefile'
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