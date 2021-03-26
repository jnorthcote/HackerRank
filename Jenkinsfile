pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    environment {
      DATA_DEF = ""
    }
    stages {
      stage('Data') {
        steps {
          script {
            switch(params.CHALLENGE) {
              case 'socks':
                env.DATA_DEF = '1 1 2 2 3 3 3'
                break;
              case 'valleys':
                env.DATA_DEF = 'DDUDUUUUDDUDDU'
                break;
              case 'jumps':
                env.DATA_DEF = '0 0 1 0 0 1 0'
                break;
              default:
                env.DATA_DEF = 'Nope'
                break;
            }
            echo "env.DATA_DEF ${env.DATA_DEF}"
          }
        }
      }
      stage('Challenge') {
          input {
            message "Challenge Data"
            parameters {
              string(name: 'DATA', defaultValue: env.DATA_DEF, description: 'Challenge data')
            }
          }
          steps {
              echo "Challenge def: ${CHALLENGE}"
              echo "Data      def: ${DATA}"
          }
      }
    }
}
