#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying application..'
                sh 'python3 warehouse_management/main.py --action add --name "New Book" --quantity 10 --price 19.99 --type book'
                sh 'python3 warehouse_management/main.py --action show'
            }
        }
    }
}
