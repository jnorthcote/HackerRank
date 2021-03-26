pipeline {
    agent none
    stages {
      stage('Challenge') {
          script {
            properties([
                parameters([
                  [
                    choiceType: 'PT_SINGLE_SELECT', description: '', filterLength: 1, filterable: false, name: 'CHALLENGE', randomName: 'choice-parameter-3528404535625',
                      script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: ''],
                      script: [classpath: [], sandbox: false, script: "return ['socks', 'valleys', 'jumps']"]]
                  ],
                  [
                    choiceType: 'ET_TEXT_BOX', description: '', name: 'DATA', omitValueField: false, randomName: 'choice-parameter-3528424397275', referencedParameters: 'Challenge',
                      script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: 'return \'\''],
                      script: [classpath: [], sandbox: false, script: "switch(Challenge) { case 'socks': return '1 1 2 2 3 3 3' case 'valleys': return 'DDUDUUUUDDUDDU' case 'jumps': return '0 0 1 0 0 1 0'}"]]
                  ]
                ])
            ])
          }
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
