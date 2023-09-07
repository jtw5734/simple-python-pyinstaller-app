pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {

        stage('Deliver') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'python:3.11.5-alpine3.18'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
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