pipeline {
    agent none
    parameters {
        choice(name: 'CHALLENGE', choices: ['utree', 'socks', 'valleys', 'jumps'], description: 'Pick a Challenge')
    }
    environment {
      DATA_DEF = "XXX"
    }
    stages {
      stage('Data') {
        steps {
          script {
            try {
              switch(params.CHALLENGE) {
                case 'utree':
                  DATA_DEF = '0 1 4'
                  break;
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
            } catch (Exception e) {
              echo "${e}"
            }
          }
          echo "env.DATA_DEF ${DATA_DEF}"
        }
      }
      stage('Challenge') {
          agent {
            label 'python-agent'
          }
          steps {
            container('python') {
              echo "Challenge def: ${CHALLENGE} par: ${params.CHALLENGE}"
              dir ('src/') {
                sh("python -u main.py ${CHALLENGE} ${DATA_DEF}")
              }
            }
          }
      }
    }
}
