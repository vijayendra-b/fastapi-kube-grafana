pipeline {

    agent any

    environment {
        IMAGE_NAME = "vijayendra1/inventory-api"
        IMAGE_TAG  = "${BUILD_NUMBER}"
        EC2_HOST   = "44.203.179.14"
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                docker build \
                -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Push Docker Image') {
            steps {

                withCredentials([
                    usernamePassword(
                        credentialsId: 'b799765c-9aab-4075-8537-541d450e7f9d',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh """
                    echo \$DOCKER_PASS | docker login \
                    -u \$DOCKER_USER \
                    --password-stdin

                    docker push ${IMAGE_NAME}:${IMAGE_TAG}

                    docker logout
                    """
                }
            }
        }

        stage('Deploy to AWS K3s Using Helm') {
            steps {

                sshagent(['aws-ec2-key']) {

                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} '

                    cd /home/ubuntu/final-capstone-inventory-api

                    git pull origin main
                    
                    export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

                    cd /home/ubuntu/final-capstone-inventory-api
                    ls -l

                    helm upgrade --install inventory-api ./helm-chart \
                    --set image.repository=${IMAGE_NAME} \
                    --set image.tag=${IMAGE_TAG}

                    kubectl rollout status deployment/inventory-api --timeout=180s
                    '
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {

                sshagent(['aws-ec2-key']) {

                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} '

                    export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

                    echo "========================="
                    echo "Helm Releases"
                    echo "========================="
                    helm list

                    echo "========================="
                    echo "Pods"
                    echo "========================="
                    kubectl get pods

                    echo "========================="
                    echo "Services"
                    echo "========================="
                    kubectl get svc

                    '
                    """
                }
            }
        }

        stage('Application Health Check') {
            steps {

                sh """
                sleep 30

                curl -f http://${EC2_HOST}:8000/health
                """
            }
        }
    }

    post {

        success {
            echo "SUCCESS: Inventory API deployed successfully"
        }

        failure {
            echo "FAILURE: Deployment failed"
        }

        always {

            sh """
            docker image prune -f || true
            """
        }
    }
}