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
                inheritFrom 'python'
                workingDir '/home/jenkins'
                idleMinutes 5
              }
            }
            steps {
              container('python') {
                echo "Challenge ${params.CHALLENGE}"
                dir ('src/') {
                  sh("python -u main.py ${params.CHALLENGE} 1 3 3 2")
                }
              }
            }
        }
    }
}
