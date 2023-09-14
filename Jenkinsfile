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
                }
            }
            steps {
                    sh 'apt install -y python3.11'
                    sh 'python -m venv ./venv'
                    sh 'source venv/bin/activate'
                    sh 'sudo pip install -r sources/requirements.txt'
                    sh 'python -m py_compile sources/add2vals.py sources/calc.py'

                    sh 'pip list >> abcd'
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