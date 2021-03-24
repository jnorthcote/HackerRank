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
                    string(name: 'DATARRAY', defaultValue: '1 1 2 2 3 3 3', description: 'Challenge data')
                }
            }
            steps {
              container('python') {
                echo "Challenge ${params.CHALLENGE} ${params.DATARRAY}"
                dir ('src/') {
                  sh("python -u main.py ${params.CHALLENGE} ${params.DATARRAY}")
                }
              }
            }
        }
    }
}
