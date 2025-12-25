pipeline {
  agent {
    docker {
      image 'python:3.11'
      args '-u root'
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
        sh '''
          python --version
          pip --version
          pip install -r requirements.txt
        '''
      }
    }

    // stage('Run tests') {
    //   steps {
    //     sh '''
    //       pytest -v
    //     '''
    //   }
    // }
  }
}
