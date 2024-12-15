# Wisecow Application Deployment

This repository contains files for deploying the Wisecow application using Docker, Kubernetes, and GitHub Actions.

## Steps to Run the Application

### 1. Build Docker Image
Run these commands to build and test the Docker image locally:
```bash
docker build -t wisecow:latest .
docker run -p 5000:5000 wisecow:latest
