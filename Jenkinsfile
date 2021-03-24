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
            steps {
              input {
                  message "Challenge Selection"
                  parameters {
                      choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
                      string(name: 'DATA', defaultValue: '1 1 2 2 3 3 3', description: 'Challenge data')
                  }
              }
              container('python') {
                echo "Challenge ${params.CHALLENGE}"
                dir ('src/') {
                  sh("python -u main.py ${params.CHALLENGE} ${params.DATA}")
                }
              }
            }
        }
    }
}
