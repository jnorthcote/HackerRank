pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    environment {
        DATA_DEF = "IDD"
    }
    stages {
      stage('Data') {
        steps {
          script {
            switch(params.CHALLENGE) {
              case 'socks':
                DATA_DEF = '1 1 2 2 3 3 3'
                break;
              case 'valleys':
                DATA_DEF = 'DDUDUUUUDDUDDU'
                break;
              case 'jumps':
                DATA_DEF = '0 0 1 0 0 1 0'
                break;
              default:
                DATA_DEF = 'Nope'
                break;
            }
            echo "env.DATA_DEF ${env.DATA_DEF} ${DATA_DEF}"
          }
        }
      }
      stage('Challenge') {
          agent {
            label 'python-agent'
          }
          input {
            message "Challenge Data"
            parameters {
              string(name: 'DATA', defaultValue: DATA_DEF?:"", description: 'Challenge data')
            }
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
