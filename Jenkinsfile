#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying application..'
                sh 'python main.py' // Запуск основного скрипту
            }
        }
    }
}
