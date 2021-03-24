pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    stages {
        stage('Challenge') {
            agent {
              kubernetes {
                defaultContainer 'jnlp'
                inheritFrom 'default'
                workingDir '/home/jenkins'
                idleMinutes 5
              }
            }
            steps {
                echo "Challenge ${params.CHALLENGE}"
                sh 'ls -alr'
            }
        }
    }
}
