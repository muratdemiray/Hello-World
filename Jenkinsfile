#!/usr/bin/env groovy

pipeline {

    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'docker build --force-rm -t "hello-world:test" .'
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