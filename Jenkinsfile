pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    stages {
        stage('Challenge') {
            agent {
              kubernetes {
                label 'python'
                idleMinutes 5
                defaultContainer 'python'
              }
            }
            steps {
                echo "Challenge ${CHALLENGE}"
                sh 'ls -alr'
            }
        }
    }
}
