pipeline {
    agent none
    stages {
        stage('Challenge') {
            agent {
              kubernetes {
                defaultContainer 'jnlp'
                inheritFrom 'default'
                idleMinutes 5
              }
            }
            steps {
                echo "Challenge ${CHALLENGE}"
                sh 'ls -alr'
            }
        }
    }
}
