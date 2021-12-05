#!/usr/bin/env groovy

pipeline {

    agent {
        docker {
            image 'node'
            args '-u root'
        }
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh '. ./build-docker-test-image.sh'
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