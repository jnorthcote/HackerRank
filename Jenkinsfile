pipeline {
    agent any
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    stages {
        stage('Challenge') {
            agent { docker 'python:alpine' }
            steps {
                echo "Challenge ${CHALLENGE}"
                sh 'ls -alr'
            }
        }
    }
}
