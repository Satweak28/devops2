pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git branch:'main', url:'https://github.com/Satweak28/devops.git' , credentialsId: 'github-token'

      }
    }
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Test') {
      steps {
        sh 'echo "No tests yet"'
      }
    }
    stage('Deploy') {
      steps {
        sh 'python app.py &'
      }
    }
  }
}
