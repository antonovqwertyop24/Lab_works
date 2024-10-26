#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Deploy') {
            steps {
                echo 'Deploying application..'
                sh 'python3 warehouse_management/test_warehouse.py'
            }
        }
    }
}
