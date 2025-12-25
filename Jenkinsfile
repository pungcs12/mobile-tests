pipeline {
  agent {
    kubernetes {
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
    APPIUM_SERVER_URL = "http://host.docker.internal:4723"
  }

  stages {

    stage('Checkout source') {
      steps {
        checkout scm
      }
    }

    stage('Install dependencies') {
      steps {
        container('pytest') {
          sh '''
            python --version
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
            pytest tests --junitxml=report.xml
          '''
        }
      }
    }
  }

  post {
    always {
      junit 'report.xml'
    }
  }
}
