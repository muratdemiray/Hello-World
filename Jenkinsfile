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
        stage('Run') {
            steps {
                echo 'Deploying...'  
              //  bat 'helm uninstall  flaskapp'     
                bat 'helm uninstall flaskapp ; helm install flaskapp helm-app/' 
                echo 'http://localhost'       

            }
        }
    }
}