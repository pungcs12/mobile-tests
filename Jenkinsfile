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

  environment {
    APPIUM_SERVER = "http://host.docker.internal:4723"
  }

  stages {

    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        container('pytest') {
          sh '''
            python -V
            pip install --upgrade pip
            pip install -r requirements.txt
          '''
        }
      }
    }

    stage('Run tests') {
      steps {
        container('pytest') {
          sh '''
            pytest mobile-tests -v
          '''
        }
      }
    }
  }
}
