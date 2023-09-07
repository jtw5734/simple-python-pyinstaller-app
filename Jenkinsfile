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
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                sh 'python -V >> abcd'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
            post {
                success {
                    archiveArtifacts "./abcd"
                }
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'python:3.11.5-alpine3.18'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "python>> abcd"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/abcd"
                }
            }
        }
    }
}