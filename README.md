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