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
        stage('Publish'){
            steps {
                // configure registry
                docker.withRegistry('https://106447319060.dkr.ecr.eu-central-1.amazonaws.com', 'ecr:eu-central-1:7c87d4ce-424d-425e-ada8-9e4f45ed5ac3') {

                // build image
                def customImage = docker.build("hello-world:${env.BUILD_ID}")

                // push image
                customImage.push()
                }
            }
        }
        stage('Run') {
            steps {
                echo 'Deploying...'  
              //  bat 'helm uninstall  flaskapp'     
                bat 'helm upgrade --install flaskapp helm-app/' 
                echo 'http://localhost'       


            }
        }
    }
}
