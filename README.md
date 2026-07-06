# e2e-pipeline-to-deploy-llm
# End-to-End LLM Pipeline on AWS EKS

## 🚀 Project Overview

This project demonstrates a fully automated CI/CD pipeline for deploying a Large Language Model (LLM) application.

It includes:
    1. **FastAPI** app serving a pre-trained model (GPT-2).
    2. **Docker** containerization.
    3. **Kubernetes (EKS)** orchestration on AWS.
    4. Auto-scaling and Load Balancing capabilities.

## 🛠️ Tech Stack

    - Python, FastAPI, Hugging Face Transformers
    - Docker
    - Kubernetes (AWS EKS)
    - AWS Load Balancer Service

## 🏗️ Architecture Diagram

*(Here is where you will take a screenshot of your `kubectl get svc` output or draw a simple diagram)*

1. User Request -> AWS Load Balancer -> K8s Service -> Pods -> LLM Model

## ⚙️ Local Development (Minikube)

```bash
minikube start
docker build -t my-image .
docker push my-image
kubectl apply -f k8s/
```

## ☁️ AWS EKS Deployment

Prerequisites

    - AWS CLI configured with Admin Access
    - `eksctl` installed
    - Docker Hub account

## Steps

1. Create Cluster:

 `eksctl create cluster --name my-cluster --region eu-west-1`

2. Update Kubeconfig:

 `aws eks update-kubeconfig --name my-cluster`

3. Deploy App:

 `kubectl apply -f k8s/`

## Scaling

For horizontal scaling:

    `kubectl scale deployment llm-app-deployment --replicas=3`

