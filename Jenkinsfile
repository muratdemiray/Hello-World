#!/usr/bin/env groovy

pipeline {

    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat './scripts/build-docker-test-image.sh'
                bat 'docker image ls'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'                             
            }
        }
    }
}