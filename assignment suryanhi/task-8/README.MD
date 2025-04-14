### In this solution i have taken a simple ai/ml model  that classifies iris flowers based on petal/sepal length & width.

in the app-code i have provided the source code 
## step1
firstly i have dockerized this model after creating the docker image i pushed this image(iris-api) to my docker registery 
in this solution i have taken minikube cluster to deploy the application  
 
## step2 
 i have created a deloyment file which will create a pod than runs the docker image which i have created before
 and to implement this run:
 ```bash
 kubectl apply -f deployment.yaml
 ```
this will create a pod that runs that docker image 

## step3
then i created a service.yaml file for creating the api endpoints and user can access the application to create this run:
```bash
kubectl apply -f service.yaml
```
after this whole procedure the task will be completed

