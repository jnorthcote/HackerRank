pipeline {
    agent none
    stages {
      stage('Challenge') {
        input {
            message 'Select Challenge'
            parameters {
    [choiceType: 'PT_SINGLE_SELECT', description: '', filterLength: 1, filterable: false, name: 'Challenge', randomName: 'choice-parameter-4745339100865', script: [$class: 'GroovyScript', fallbackScript: [classpath: [], sandbox: false, script: ''], script: [classpath: [], sandbox: false, script: 'return [\'socks\',\'valleys\']']]]
  }
}
          }
          agent {
            label 'python-agent'
          }
          steps {
            container('python') {
              echo "Challenge def: ${Challenge} par: ${params.Challenge}"
              echo "Data      def: ${Data} par: ${params.Data}"
              dir ('src/') {
                sh("python -u main.py ${Challenge} ${Data}")
              }
            }
          }
      }
    }
}
