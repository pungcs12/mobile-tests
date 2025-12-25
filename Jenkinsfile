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

  options {
    timestamps()
  }

  environment {
    // Change this to your Mac IP (NOT localhost)
    APPIUM_SERVER_URL = "http://172.25.91.253:4723/wd/hub"
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
            python --version
            pip install --upgrade pip
            pip install -r requirements.txt
          '''
        }
      }
    }
  }
}
