pipeline {
    agent none
#    parameters {
#        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
#    }
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
