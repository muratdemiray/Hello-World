#!/usr/bin/env groovy

pipeline {

    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                bat 'docker build --force-rm -t "hello-world:latest" .'
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