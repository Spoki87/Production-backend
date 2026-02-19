pipeline {
    agent any

        options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Clean workspace') {
            steps {
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

    environment {
        IMAGE_NAME = "production-backend"
        CONTAINER_NAME = "production-backend"

        SECRET_KEY = credentials('SECRET_KEY')          
        JWT_SECRET_KEY = credentials('JWT_SECRET_KEY')   
        JWT_EXPIRATION_TIME = credentials('JWT_EXPIRATION_TIME')               
        DATABASE_URL = credentials('DATABASE_URL')       
    }

    stages {

        stage('Clone') {
            steps {
                sh 'rm -rf $WORKSPACE/* $WORKSPACE/.* || true'
                sh 'git clone -b main https://github.com/Spoki87/Production-backend.git .'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh '''
                docker stop $CONTAINER_NAME || true
                docker rm $CONTAINER_NAME || true
                '''
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                docker run -d \
                --name $CONTAINER_NAME \
                -p 5000:5000 \
                -e SECRET_KEY=$SECRET_KEY \
                -e JWT_SECRET_KEY=$JWT_SECRET_KEY \
                -e JWT_EXPIRATION_TIME=$JWT_EXPIRATION_TIME \
                -e DATABASE_URL=$DATABASE_URL \
                $IMAGE_NAME:latest
                '''
            }
        }
    }
}
