pipeline {
    agent none
    stages {
        stage('Challenge') {
            agent {
              kubernetes {
                defaultContainer 'jnlp'
                inheritFrom 'python'
                workingDir '/home/jenkins'
                idleMinutes 5
              }
            }
            input {
                message "Challenge Selection"
                parameters {
                    choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
                }
            }
            steps {
              container('python') {
                echo "Challenge ${params.CHALLENGE}"
                dir ('src/') {
                  sh("python -u main.py ${params.CHALLENGE} 11 22 11 33 44 22")
                }
              }
            }
        }
    }
}
