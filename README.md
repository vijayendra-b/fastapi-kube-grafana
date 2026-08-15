# Cloud Native Inventory Management Platform

## Project Overview

The Cloud Native Inventory Management Platform is a Kubernetes-based Inventory Management API developed using FastAPI and deployed on AWS. The solution demonstrates containerization, orchestration, monitoring, scalability, and Helm-based application management.

The project is designed to showcase modern DevOps and Cloud-Native practices including:

- FastAPI-based REST API
- Docker containerization
- Kubernetes (K3s)
- Helm deployments
- PostgreSQL database deployment
- Prometheus monitoring
- Grafana dashboards
- Horizontal scaling using Helm replica configuration
- AWS EC2 infrastructure

---

# Architecture

```
Users
   │
   ▼

AWS EC2 (Ubuntu)
   │
   ▼

K3s Kubernetes Cluster
   │
   ├── Inventory API (FastAPI)
   ├── PostgreSQL
   └── Monitoring Stack
         │
         ├── Prometheus
         └── Grafana 
```

# Cloud Native Inventory Management Platform

## Project Overview

The Cloud Native Inventory Management Platform is a Kubernetes-based Inventory Management API developed using FastAPI and deployed on AWS. The solution demonstrates containerization, orchestration, monitoring, scalability, and Helm-based application management.

The project is designed to showcase modern DevOps and Cloud-Native practices including:

- FastAPI-based REST API
- Docker containerization
- Kubernetes (K3s)
- Helm deployments
- PostgreSQL database deployment
- Prometheus monitoring
- Grafana dashboards
- Horizontal scaling using Helm replica configuration
- AWS EC2 infrastructure

---

# Architecture

```text
Users
   │
   ▼

AWS EC2 (Ubuntu)
   │
   ▼

K3s Kubernetes Cluster
   │
   ├── Inventory API (FastAPI)
   ├── PostgreSQL
   └── Monitoring Stack
         │
         ├── Prometheus
         └── Grafana
```

Technology Stack
Layer	TechnologyCloud	AWS EC2
Operating System	Ubuntu
Container Runtime	Docker
Orchestration	K3s Kubernetes
Package Manager	Helm
Backend API	FastAPI
Database	PostgreSQL
Monitoring	Prometheus
Visualization	Grafana
Project Objectives
Objective 1

Deploy applications using Helm Charts.

✅ Implemented

Objective 2

Implement centralized monitoring and observability.

✅ Implemented using Prometheus and Grafana

Objective 3

Demonstrate scalable Kubernetes architecture.

✅ Implemented using configurable replicaCount through Helm

Repository Structure:
```
final-capstone-inventory-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routes/
│       ├── products.py
│       └── orders.py
│
├── helm-chart/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       └── service.yaml
│
├── Dockerfile
├── requirements.txt
└── README.md
```
Application Endpoints

Health Check

```bash
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

Metrics Endpoint

```bash
GET /metrics
```


Provides Prometheus-compatible metrics used for monitoring and visualization.

Docker Deployment
Build Docker Image

```bash
docker build -t inventory-api:v1 .
```

Run Container

```bash
docker run -d \
-p 8000:8000 \
--name inventory-api \
inventory-api:v1
```

Kubernetes Deployment

Check Cluster

```bash
kubectl get nodes
```

Check Pods

```bash
kubectl get pods -A
```

Helm Deployment

Install Application

```bash
helm install inventory-api ./helm-chart
```

Upgrade Application

```bash
helm upgrade inventory-api ./helm-chart
```

View Releases

```bash
helm list -A
```

View Revision History

```bash
helm history inventory-api
```

Scaling Using Helm

Current scaling configuration resides in:

```bash
replicaCount: 2
```

Example upgrade:

```bash
helm upgrade inventory-api ./helm-chart \
--set replicaCount=4
```

Verify:

```bash
kubectl get pods
```


This creates additional application replicas automatically.

PostgreSQL Deployment

PostgreSQL is deployed using the Bitnami Helm chart.

Install command:

```bash
helm install postgres bitnami/postgresql
```

Verify database pod:

```bash
kubectl get pods
```

Example:

```
postgres-postgresql-0
```

Monitoring Stack

Monitoring components are deployed using:

```bash
helm install monitoring \
prometheus-community/kube-prometheus-stack \
-n monitoring \
--create-namespace
```

Components
- Prometheus
- Grafana
- AlertManager
- Node Exporter
- Kube State Metrics

Grafana Access

Port Forward:

```bash
kubectl port-forward svc/monitoring-grafana \
3000:80 \
-n monitoring \
--address 0.0.0.0
```

Access:

```
http://<EC2-PUBLIC-IP>:3000
```

Default Username:

```
admin
```

Retrieve Password:

```bash
kubectl get secret monitoring-grafana \
-n monitoring \
-o jsonpath="{.data.admin-password}" | base64 -d
```

Prometheus

Prometheus automatically scrapes Kubernetes metrics through the kube-prometheus-stack deployment.

Typical metrics collected:

- Node CPU Usage
- Node Memory Usage
- Pod Metrics
- Application Metrics
- Kubernetes Resource Metrics
CI/CD Pipeline (Jenkins)

Proposed CI/CD workflow:

```
Developer Commit
        ↓
Git Repository
        ↓
Jenkins Pipeline
        ↓
Docker Build
        ↓
Docker Hub Push
        ↓
Helm Upgrade
        ↓
AWS EC2
        ↓
K3s Kubernetes
        ↓
Rolling Deployment
        ↓
Prometheus & Grafana Monitoring
```

Useful Commands

**Cluster:**
```bash
kubectl get nodes
```

**Pods:**
```bash
kubectl get pods -A
```

**Services:**
```bash
kubectl get svc
```

**Helm Releases:**
```bash
helm list -A
```

**Helm History:**
```bash
helm history inventory-api
```

**Monitoring Pods:**
```bash
kubectl get pods -n monitoring
```

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Metrics:**
```bash
curl http://localhost:8000/metrics
```

Future Enhancements

The following enhancements can be incorporated in future releases:

- OpenTelemetry-based tracing
- Loki log aggregation
- Fluent Bit log shipping
- Horizontal Pod Autoscaler (HPA)
- AWS Secrets Manager integration
- GitOps using ArgoCD
- Automated CI/CD using Jenkins
Conclusion

This project demonstrates a complete cloud-native application deployment using FastAPI, Docker, Kubernetes, Helm, Prometheus, Grafana, PostgreSQL, and AWS. The solution showcases container orchestration, monitoring, observability, and scalability while following modern DevOps practices.

# Installation and Deployment Guide

This guide explains how to deploy the Cloud Native Inventory Management Platform in your own AWS account.

---

## Prerequisites

Ensure the following tools are available:

- AWS Account
- EC2 Instance (Ubuntu 24.04 recommended)
- Git
- Docker
- Helm
- kubectl
- K3s Kubernetes
- Docker Hub Account

---

## Step 1: Launch an EC2 Instance

Create an Ubuntu EC2 instance with at least:

```text
Instance Type: t3.medium
vCPU: 2
Memory: 4 GB
Storage: 20 GB
```

Configure the Security Group:

```text
22    SSH
3000  Grafana
8000  FastAPI API
9090  Prometheus (Optional)
```

---

## Step 2: Connect to EC2

```bash
ssh -i <key.pem> ubuntu@<EC2_PUBLIC_IP>
```

---

## Step 3: Install K3s

```bash
curl -sfL https://get.k3s.io | sh -
```

Configure kubectl:

```bash
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
```

Verify installation:

```bash
kubectl get nodes
```

Expected:

```text
Ready
```

---

## Step 4: Install Helm

```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

Verify:

```bash
helm version
```

---

## Step 5: Clone Repository

```bash
git clone <repository-url>
```

```bash
cd fastapi-kube-grafana
```

---

## Step 6: Build and Push Docker Image

Update `helm-chart/values.yaml`:

```yaml
image:
  repository: <dockerhub-username>/inventory-api
  tag: "v1"
```

Build image:

```bash
docker build -t <dockerhub-username>/inventory-api:v1 .
```

Login to Docker Hub:

```bash
docker login
```

Push image:

```bash
docker push <dockerhub-username>/inventory-api:v1
```

---

## Step 7: Deploy PostgreSQL

Add Helm repository:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

Install PostgreSQL:

```bash
helm install postgres bitnami/postgresql
```

Verify:

```bash
kubectl get pods
```

---

## Step 8: Deploy Monitoring Stack

Add Prometheus Helm repository:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```

Install monitoring stack:

```bash
helm install monitoring \
prometheus-community/kube-prometheus-stack \
-n monitoring \
--create-namespace
```

Verify:

```bash
kubectl get pods -n monitoring
```

---

## Step 9: Deploy Inventory API

Install application:

```bash
helm install inventory-api ./helm-chart
```

Verify deployment:

```bash
kubectl get pods
```

Expected:

```text
inventory-api-xxxxx
inventory-api-yyyyy
postgres-postgresql-0
```

---

## Step 10: Verify Application

Health endpoint:

```bash
curl http://<EC2_PUBLIC_IP>:8000/health
```

Expected:

```json
{
  "status": "healthy"
}
```

Metrics endpoint:

```bash
curl http://<EC2_PUBLIC_IP>:8000/metrics
```

---

## Step 11: Access Grafana

Start port forwarding:

```bash
kubectl port-forward \
svc/monitoring-grafana \
3000:80 \
-n monitoring \
--address 0.0.0.0
```

Access:

```text
http://<EC2_PUBLIC_IP>:3000
```

Get Grafana password:

```bash
kubectl get secret monitoring-grafana \
-n monitoring \
-o jsonpath="{.data.admin-password}" | base64 -d
```

Login:

```text
Username: admin
Password: <retrieved-password>
```

---

## Step 12: Verify Prometheus Monitoring

Verify ServiceMonitor:

```bash
kubectl get servicemonitor -n monitoring
```

Check Prometheus Targets:

```text
Status → Target Health
```

Confirm:

```text
inventory-api-monitor
2/2 UP
```

---

## Step 13: Scale Application

Scale replicas using Helm:

```bash
helm upgrade inventory-api ./helm-chart \
--set replicaCount=4
```

Verify:

```bash
kubectl get pods
```

Expected:

```text
4 Inventory API Pods
```

---

## Uninstall Resources

Remove Inventory API:

```bash
helm uninstall inventory-api
```

Remove PostgreSQL:

```bash
helm uninstall postgres
```

Remove Monitoring Stack:

```bash
helm uninstall monitoring -n monitoring
```

Delete monitoring namespace:

```bash
kubectl delete namespace monitoring
```

---

## Project Verification Checklist

- [ ] EC2 Instance Running
- [ ] K3s Installed
- [ ] Helm Installed
- [ ] Docker Image Available in Docker Hub
- [ ] PostgreSQL Running
- [ ] Inventory API Running
- [ ] Prometheus Running
- [ ] Grafana Accessible
- [ ] ServiceMonitor Active
- [ ] Inventory Metrics Visible in Prometheus
- [ ] Inventory Dashboard Visible in Grafana
- [ ] Helm-Based Scaling Verified