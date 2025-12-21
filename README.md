# Humana AI/ML DevOps Platform Demo

Governance-first AI/ML DevOps demo with GitOps, DORA metrics, and multi-cloud CI/CD (AWS, Azure, GCP, on-prem).


This repository demonstrates a governance-first AI/ML DevOps platform designed for regulated, enterprise environments. It showcases standardized CI/CD pipelines, GitOps-based deployments, DORA metrics, KPI dashboards, and security/compliance controls across on-prem and multi-cloud Kubernetes platforms (AWS EKS, Azure AKS, GCP GKE).

## DORA Metrics & Observability

This project includes a lightweight DORA metrics pipeline:
- CI/CD and GitOps metrics are exposed via a custom exporter
- Prometheus scrapes metrics
- Grafana dashboards provide leadership visibility

Tracked metrics:
- Deployment Frequency
- Lead Time for Changes

Dashboards are version-controlled and provisioned as code.
