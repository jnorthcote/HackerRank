pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
        string(name: 'DATA', defaultValue: params.DATA ?:'1 1 2 2 3 3 3', description: 'Challenge data')
    }
    stages {
        stage('Challenge') {
            agent {
              label 'python-agent'
            }
            steps {
              container('python') {
                echo "Challenge def: ${CHALLENGE} par: ${params.CHALLENGE}"
                echo "Data      def: ${DATA} par: ${params.DATA}"
                dir ('src/') {
                  sh("python -u main.py ${CHALLENGE} ${DATA}")
                }
              }
            }
        }
    }
}
