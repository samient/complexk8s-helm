# complexk8s-helm

Multi-Tier Application Deployment with Helm
This solution deploys a 3-tier application with:

Frontend (Nginx web server)

Backend (Node.js API server)

Database (PostgreSQL with Persistent Volume)

Ingress (for external access)
===============================================
multi-tier-app/
├── Chart.yaml          # Helm chart metadata
├── values.yaml         # Default configuration
├── templates/          # Kubernetes manifests
│   ├── frontend/
│   │   ├── deployment.yaml
│   │   ├── service.yaml
│   │   └── ingress.yaml
│   ├── backend/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── database/
│       ├── statefulset.yaml
│       ├── service.yaml
│       └── pvc.yaml
└── requirements.yaml   # Dependencies (if any)
