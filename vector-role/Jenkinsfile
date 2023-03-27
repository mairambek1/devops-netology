pipeline{
    agent{
        label 'docker'
    }
    stages{
        stage('checkout git'){
            steps{
                dir('vector-role'){
                    git branch: 'main', credentialsId: 'de9af9bd-539e-4d01-beff-8e6767ca2c22', url: 'git@github.com:nkiselyov/vector-role.git'
                }
            }
        }
        stage('install dependencies'){
            steps{
                dir('vector-role'){
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('run molecule'){
            steps{
                dir('vector-role'){
                    sh 'molecule test'
                }
            }
        }
    }
}