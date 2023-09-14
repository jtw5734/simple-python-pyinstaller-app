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
                    sh 'sudo apt-get update -y'
                    sh 'sudo apt-get install python3.11 python3-distutils -y'
                    sh 'sudo apt-get install python3-pip -y'
                    sh 'sudo apt-get install binutils -y'
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