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
                    sh 'python gh_release.py'
            }
            post {
                success {
                    archiveArtifacts "dist/dot_local_api"
                    archiveArtifacts "abcd"
                }
            }
        }
        stage('github release') {
            agent {
                docker {
                    image 'python:3.11'
                    args '-u root --privileged'
                }
            }
            steps {
                    sh 'apt-get install binutils'
                    sh 'ls -l > abcd'
                    sh 'pip install requests==2.21.0'
                    sh 'python gh_release.py > release.log'
            }
            post {
                success {
                    archiveArtifacts "release.log"
                }
            }
        }

    }
}