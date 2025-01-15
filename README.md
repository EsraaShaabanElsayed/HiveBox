
# **HiveBox: A Scalable DevOps Application**

![DevOps](https://img.shields.io/badge/DevOps-Kubernetes-blue)  
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)  

## **📜 Overview**

HiveBox is a hands-on DevOps project designed to track environmental data from sensors via a RESTful API. Inspired by real-world applications, this project emphasizes scalable architecture, modern DevOps practices, and observability.

---

## **🌟 Key Contributions**

### 1. **API Development**
   - Developed RESTful endpoints:
     - `/version` to retrieve the application version.
     - `/temperature` to calculate average temperature from sensors.
     - `/metrics` for Prometheus integration.
     - `/store` to save data into MinIO storage.
   - Designed and implemented robust error handling and response structure.

### 2. **Containerization**
   - Created a **Dockerfile** to package the application.
   - Built and tested Docker images for consistent deployment.

### 3. **CI/CD Pipeline**
   - Configured **GitHub Actions** to automate:
     - Code linting and testing.
     - Docker image builds.
     - Deployment to Kubernetes clusters.

### 4. **Kubernetes Deployment**
   - Wrote **Helm charts** for deploying the application to Kubernetes.
   - Configured **Kubernetes manifests** with:
     - Deployments
     - Services
     - ConfigMaps and Secrets
   - Implemented readiness and liveness probes.

### 5. **Monitoring and Observability**
   - Integrated **Prometheus** for metrics collection.
   - Configured **Grafana** dashboards for visualizing:
     - API performance metrics.
     - Resource usage and system health.

### 6. **Storage Integration**
   - Connected the application with:
     - **Redis** for caching sensor data.
     - **MinIO** for storing structured data files.

### 7. **Documentation**
   - Authored comprehensive project documentation, including setup guides and architecture diagrams.

---

## **⚙️ Tools and Technologies**

- **Programming**: Python (Flask) 
- **Containerization**: Docker  
- **Orchestration**: Kubernetes, Helm  
- **CI/CD**: GitHub Actions  
- **Monitoring**: Prometheus, Grafana  
- **Storage**: Redis, MinIO  
- **Infrastructure as Code**: Terraform

---



## **📦 Setup and Usage**

### Prerequisites

- Docker and Docker Compose
- Kubernetes cluster (Minikube, Kind, or cloud-based)
- Redis and MinIO instances

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/EsraaShaabanElsayed/HiveBox.git
   cd HiveBox
   ```

2. Build the Docker image:
   ```bash
   docker build -t hivebox:v1 .
   ```

3. Deploy to Kubernetes:
   ```bash
   helm install hivebox ./charts
   ```

4. Access endpoints:
   - `/version`: `http://<k8s-service-ip>:<port>/version`
   - `/metrics`: `http://<k8s-service-ip>:<port>/metrics`

---

## **📊 Project Roadmap**

1. **Phase 1**: Build basic API endpoints and Dockerize the application.
2. **Phase 2**: Implement CI/CD pipelines with GitHub Actions.
3. **Phase 3**: Deploy to Kubernetes and configure monitoring with Prometheus and Grafana.
4. **Phase 4**: Add advanced features like caching and scalable storage.
5. **Phase 5**: Optimize and document for production-readiness.

---

## **👨‍💻 About Me**

I am Esraa Shaaban, a passionate DevOps Engineer with expertise in cloud-native tools, CI/CD pipelines, and infrastructure automation. This project showcases my technical skills and hands-on experience in building scalable systems.
