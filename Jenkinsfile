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

    stage('Run tests') {
      steps {
        container('pytest') {
          sh 'pytest --junitxml=reports/result.xml'
        }
      }
    }
  }

  post {
    always {
      script {
        if (fileExists('reports/result.xml')) {
          junit 'reports/result.xml'
        }
      }
    }
  }
}