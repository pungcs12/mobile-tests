pipeline {
  agent {
    kubernetes {
      label 'mobile-test'
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

    stage('Run mobile tests') {
      steps {
        container('pytest') {
          sh '''
            pytest mobile-tests \
              --appium-url=${APPIUM_SERVER} \
              -v
          '''
        }
      }
    }
  }
}
