pipeline {
    agent any
    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-creds-file')
        TF_VAR_project_id = 'test-data-462007'
        CLUSTER_NAME = 'cluster123'
        REGION = 'us-central1'
        ZONE = 'us-central1-a'
        HELM_CHART_PATH = 'multi-tier-app'
    }
    stages {
        stage('Setup GCP Environment') {
            steps {
                script {
                    // Authenticate with GCP
                    sh """
                    gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}
                    gcloud config set project ${TF_VAR_project_id}
                    gcloud config set compute/zone ${ZONE}
                    """
                }
            }
        }
        
        stage('Configure Kubernetes Access') {
            steps {
                script {
                    // Get cluster credentials
                    sh """
                    gcloud container clusters get-credentials ${CLUSTER_NAME} \
                        --region ${REGION} \
                        --project ${TF_VAR_project_id}
                    """
                    
                    // Verify cluster access
                    sh "kubectl cluster-info"
                }
            }
        }
        
        stage('Install/Upgrade Helm Chart') {
            steps {
                script {
                    // Create namespace if not exists
                    sh """
                    kubectl create namespace production || true
                    """
                    
                    // Deploy with Helm
                    sh """
                    helm upgrade --install my-app ${HELM_CHART_PATH} \
                        --namespace production \
                        --values ${HELM_CHART_PATH}/values.yaml \
                        --atomic \
                        --timeout 5m
                    """
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                script {
                    // Check resources
                    sh """
                    kubectl get all,pvc,ingress -n production
                    """
                    
                    // Run Helm tests
                    sh "helm test my-app -n production"
                    
                    // Verify pods are running
                    sh """
                    kubectl wait --for=condition=Ready pods --all -n production --timeout=300s
                    """
                }
            }
        }
        
        stage('Smoke Test') {
            steps {
                script {
                    // Test frontend ingress (replace with your actual host)
                    sh """
                    INGRESS_IP=\$(kubectl get ingress my-app-ingress -n production -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
                    curl -v http://\$INGRESS_IP
                    """
                }
            }
        }
    }
    post {
        always {
            // Cleanup or notifications can go here
            echo "Deployment pipeline completed"
        }
        failure {
            // Send failure notification
            echo "Pipeline failed - check logs for details"
        }
    }
}