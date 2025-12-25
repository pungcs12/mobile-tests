pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Install deps') {
      steps {
        sh '''
          python3 --version || true
          pip3 install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          pytest -v
        '''
      }
    }
  }
}
