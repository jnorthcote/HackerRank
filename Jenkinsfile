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
            switch(CHALLENGE) {
              case 'socks':
                env.DATA_DEF = '1 1 2 2 3 3 3'
                break;
              case 'valleys':
                env.DATA_DEF = 'DDUDUUUUDDUDDU'
                break;
              case 'jumps':
                env.DATA_DEF = '0 0 1 0 0 1 0'
                break;
            }
          }
        }
      }
      stage('Challenge') {
          agent {
            label 'python-agent'
          }
          intput {
            parameters {
              string(name: 'DATA', defaultValue: env.DATA_DEF, description: 'Challenge data')
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
