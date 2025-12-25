pipeline {
  agent {
    kubernetes {
      defaultContainer 'pytest'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: pytest
    image: python:3.11
    command:
    - cat
    tty: true
"""
    }
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Test') {
      steps {
        container('pytest') {
          sh 'echo HELLO FROM POD'
        }
      }
    }
  }
}
