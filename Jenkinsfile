pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'ubuntu:23.04'
                    args '-u root --privileged'
                }
            }
            steps {
                    sh 'apt update -y'
                    sh 'apt install python3.11 python3-distutils -y'
                    sh 'apt install python3-pip -y'
                    sh 'apt install binutils -y'
                    sh 'pip3 install -r src/requirements.txt'
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