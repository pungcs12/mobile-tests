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

    stage('Run mobile tests') {
      steps {
        container('pytest') {
          sh '''
            mkdir -p reports
            pytest -v \
              --junitxml=reports/result.xml
          '''
        }
      }
    }
  }

  post {
    always {
      script {
        try {
          container('pytest') {
            if (fileExists('reports/result.xml')) {
              junit 'reports/result.xml'
            } else {
              echo 'No test report found, skipping junit'
            }
          }
        } catch (err) {
          echo "Post actions skipped: ${err}"
        }
      }
    }
  }
}
