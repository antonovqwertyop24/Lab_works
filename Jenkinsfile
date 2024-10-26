#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying application..'
                sh 'python3 warehouse_management/main.py' // Запуск основного скрипту
            }
        }
    }
}
