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
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'ubuntu:23.04'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "sudo apt-get update && apt-get install -y"
                    sh "sudo apt-get install python3-pip"
                    sh "sudo apt-get install python3.11"
                    sh "python -V >> abcd"
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