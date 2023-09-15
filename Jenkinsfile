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
                    
                    sh 'pip install requests'
                    sh 'python gh_release.py > release.log'

                    //sh 'apt-get install binutils'
                    //sh 'pip install -r src/requirements.txt'
                    //sh 'pyinstaller -y --clean --name dot_local_api --additional-hooks-dir ./src/extra-hooks ./src/main.py --onefile'
            }
            post {
                success {
                    //archiveArtifacts "dist/dot_local_api"
                    archiveArtifacts "release.log"
                }
            }
        }


    }
}