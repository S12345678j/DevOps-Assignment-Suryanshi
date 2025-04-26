# Hello World Kubernetes Deployment

This project demonstrates how to deploy a simple "Hello World" application using NGINX on a local Kubernetes cluster. We will use `kind` (Kubernetes in Docker) to create a local Kubernetes cluster, build a Docker image for the application, and expose the application via a `NodePort` service.

## Prerequisites

Before you begin, ensure you have the following tools installed:

- **Docker**: For building and loading the Docker image.
- **Kind**: For creating a local Kubernetes cluster. [Install Kind](https://kind.sigs.k8s.io/docs/user/quick-start/)
- **kubectl**: Kubernetes command-line tool. [Install kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## Setup and Deployment

### Step 1: Create a Simple HTML File

Create a folder named `app` in your project directory and place the following HTML file inside it.

**app/index.html:**

```html
<h1>Hello, World from Kubernetes!</h1>
```
### Step 2: Create the Kubernetes Cluster

Create a Kubernetes cluster using kind:

```bash
kind create cluster --name hello-world-cluster
```

Verify the cluster:

```bash
kubectl get nodes
```
### Step 3: Create a Docker Image for NGINX

Create a Dockerfile in the root of the project directory to build the NGINX image:

**docker/dockerfile:**

```dockerfile
FROM nginx:alpine

COPY app/index.html /usr/share/nginx/html/index.html
```

### Step 4: Build and Load the Docker Image

Build the Docker image:

```bash
docker build -t hello-world-nginx -f docker/Dockerfile .
```

**Load the Docker image into the Kind cluster:**

Run the following command to load the image into the Kind cluster:

```bash
 kind load docker-image hello-world-nginx --name hello-world-cluster
```

### Step 5: Create Kubernetes Manifests

Create two Kubernetes YAML files for the deployment and service.

**deployment.yaml:**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-world
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-world
  template:
    metadata:
      labels:
        app: hello-world
    spec:
      containers:
        - name: nginx
          image: hello-world-nginx:latest
          imagePullPolicy: Never
          ports:
            - containerPort: 80
```

**service.yaml:**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-world-service
spec:
  selector:
    app: hello-world
  type: NodePort
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      nodePort: 30001
```



### Step 6: Deploy to Kubernetes

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

**Verify the deployment and service:**
```bash
kubectl get pods
kubectl get svc
```

### Step 7: Access the Application

**Get the `NodePort` of the service:**

   To access your application from your local machine, get the port that the service is exposed on:

   ```bash
   kubectl get service hello-world-service
   ```

   Look for the `NodePort` in the output (default is `30001`).

**Access the Application in Your Browser or via cURL:**

   - On most systems (Linux/macOS), open your browser and go to:

     ```
     http://localhost:30001
     ```

   - Or, use `curl`:

     ```bash
     curl localhost:30001
     ```

**⚠️ Windows Users (PowerShell/Docker Desktop Note):**

   On Windows, especially when using Docker Desktop or PowerShell, direct access to the `NodePort` (like `localhost:30001`) might **not work** due to networking limitations.

   **Use `kubectl port-forward` instead:**

   Forward the port from the pod to your local machine:

   ```bash
   kubectl port-forward svc/hello-world-service 8080:80
   ```

   Then open your browser and 
   go to:

   ```
   http://localhost:8080
   ```