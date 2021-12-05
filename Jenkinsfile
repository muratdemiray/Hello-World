#!/usr/bin/env groovy

pipeline {

    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'build-docker-test-image.sh'
                sh 'docker image ls'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'                             
            }
        }
    }
}