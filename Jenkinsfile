pipeline {
  agent {
    kubernetes {
      label 'python-agent'
      defaultContainer 'python'
      yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
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

    stage('Install deps') {
      steps {
        container('python') {
          sh '''
            python --version
            pip --version
            pip install -r requirements.txt
          '''
        }
      }
    }

    stage('Run tests') {
      steps {
        container('python') {
          sh '''
            pytest -v
          '''
        }
      }
    }
  }
}
