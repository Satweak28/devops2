pipeline {
  agent any

  stages {
    stage('Clone') {
      steps {
        git 'https://github.com/your-username/your-flask-repo.git'
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
