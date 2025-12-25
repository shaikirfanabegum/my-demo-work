# Humana AI/ML DevOps Platform Demo

This repository demonstrates an **enterprise-grade AI/ML DevOps platform** with a strong focus on **deployment maturity, governance, observability, and reliability**, rather than cloud complexity.

The goal of this project is to showcase **how modern AI/ML services are built, deployed, monitored, and operated** in a regulated, large-scale enterprise environment (similar to Humana), using Kubernetes, Helm, GitOps principles, and platform observability.

---

## 🎯 Purpose of This Demo

This project is **not** about training a complex ML model or deploying to every cloud provider.

Instead, it focuses on:

- Standardized **application deployment patterns**
- **Cloud-agnostic, reusable infrastructure**
- **Helm-based configuration governance**
- **Production-grade observability** using Prometheus & Grafana
- **Clear separation of concerns** between application, platform, and operations
- **Enterprise DevOps & SRE maturity**

This is exactly the level expected for **Senior / Lead DevOps, SRE, or Platform Engineer interviews**.

---

## 🧠 What Are We Deploying?

We deploy a **sample AI inference API** that represents a real ML service used in production environments.

Think of it as:
> “A lightweight inference service that would normally serve predictions from a trained ML model.”

Key characteristics:
- Containerized application
- Deployed on Kubernetes
- Exposed via a Kubernetes Service
- Monitored with Prometheus
- Visualized in Grafana

The ML logic itself is intentionally simple — **the focus is the platform, not the model**.

---

## 🏗️ High-Level Architecture

GitHub Repository
│
├── Application Code (Inference API)
│
├── Helm Chart
│ ├── Deployment
│ ├── Service
│ └── Configurable values
│
├── Kubernetes Cluster (k3d / on-prem)
│
├── Platform Observability
│ ├── Prometheus (metrics collection)
│ └── Grafana (dashboards & visualization)


---

## 📂 Repository Structure



humana-ai-ml-devops-demo/
│
├── app/
│ └── inference-api/
│ └── source code for the API
│
├── helm/
│ └── inference-api/
│ ├── templates/
│ │ ├── deployment.yaml
│ │ ├── service.yaml
│ │ └── serviceaccount.yaml
│ ├── values.yaml
│ └── Chart.yaml
│
├── platform/
│ └── observability/
│ └── prometheus + grafana setup
│
└── README.md


---

## 🔧 Why Kubernetes (k3d / On-Prem)?

We intentionally deploy on **k3d (local Kubernetes)** instead of AWS/GCP/Azure.

**Why?**
- Demonstrates **cloud-agnostic design**
- Focuses on **deployment maturity**, not cloud services
- Matches real enterprise patterns where:
  - On-prem
  - Hybrid
  - Regulated environments  
  are common

> Any Kubernetes cluster (EKS, AKS, GKE) could run this **without changing the application**.

---

## 📦 Why Helm?

Helm is used to:

- Package the application in a **reusable, versioned chart**
- Separate **configuration from code**
- Enable:
  - Environment-specific values
  - Controlled rollouts
  - Governance and consistency

Key concepts demonstrated:
- `values.yaml` controls replicas, resources, labels
- Templates define Kubernetes manifests
- Same chart can be reused across environments

---

## 📊 Observability: Prometheus & Grafana

This demo includes **real platform observability**, not just a running app.

### Prometheus
- Scrapes Kubernetes and application metrics
- Collects:
  - Pod health
  - Resource usage
  - Application metrics

### Grafana
- Visualizes metrics via dashboards
- Used to answer:
  - Is the app healthy?
  - Are pods restarting?
  - Is latency increasing?
  - Is capacity sufficient?

---

## 🔐 How to Access Grafana

1. Port-forward Grafana:
   ```bash
   kubectl port-forward svc/grafana 3000:80 -n monitoring


**Open browser:**

http://localhost:3000


**Login credentials:**

Username: admin
Password: admin


**Navigate to dashboards and observe:**

Cluster health

Pod metrics

Application performance

****🚀 Deployment Flow (End-to-End)

Code exists in GitHub

Helm chart defines deployment

Application is deployed to Kubernetes

Prometheus scrapes metrics

Grafana visualizes platform health****



After deployment, you should see:

Running pods:

kubectl get pods


Active services:

kubectl get svc


Healthy metrics in Prometheus

Dashboards populated in Grafana

Stable inference API responding to requests

🧠 What This Demo Proves

This project demonstrates:

✅ Kubernetes fundamentals
✅ Helm governance and reuse
✅ Observability maturity
✅ Platform-first DevOps thinking
✅ Cloud-agnostic design
✅ SRE mindset (monitoring, reliability, visibility)
