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
                }
            }
            steps {
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