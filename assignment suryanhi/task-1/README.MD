# Deploying Python Web App on Azure App Service

##  Prerequisites

Before you start, make sure you have the following:

- ✅ Python web app (Flask/Django/FastAPI etc.)
- ✅ An [Azure account](https://portal.azure.com/)
- ✅ [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed
- ✅ [Git](https://git-scm.com/) installed
- ✅ (Optional) GitHub repository with your project

---
# Deploying Python Web App on Azure App Service

## Prerequisites

- Azure subscription ([create one here](https://azure.microsoft.com/free/))
- Python application with:
  - `requirements.txt` file listing dependencies
  - An entry point file (e.g., `app.py` for Flask/Django)
- Installed tools:
  - [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)
  - [Python](https://www.python.org/) and `pip`

---

## Steps to Deploy the App

### 1. **Prepare Your Python App**
Ensure your app runs locally:
```bash
python3 app.py
```

2. Login to Azure
Authenticate with Azure CLI:
```bash
az login
```


3. Create Resource Group
Create a new resource group or use an existing one:
 

```bash
az group create --name RG1 --location US EAST
```

4. Create an App Service Plan
Set up an App Service plan:
```bash
az appservice plan create --name <app_service_plan_name> --resource-group RG1
```

5. Create the Web App
Create the App Service:
```bash
az webapp create --name 3-tier-flask-app --resource-group RG1 --plan ASP-pythonapppgroup-95a9 (B1:1) --runtime "PYTHON:3.10"
```

```bash
az webapp create --name 3-tier-flask-app --resource-group RG1  --runtime "PYTHON:3.10"
```

6. Deploy the App
Package your application into a zip file:
```bash
zip -r app.zip .
```

Deploy the app using Azure CLI:
```bash
az webapp deploy --resource-group  RG1 --name 3-tier-flask-app --src-path app.zip
```

7. Set Application Settings (Optional)
Configure environment variables for your app:
```bash
az webapp config appsettings set --name 3-tier-flask-app --resource-group  RG1 --settings ENV_VAR_NAME=value
```

8. Access Your App
Get the public URL for your app:
az webapp show --name 3-tier-flask-app --resource-group  RG1 --query defaultHostName --output tsv


Visit the URL in your browser:
http://pythonmsgapp-dfa9dzh9bxewbvc4.eastus-01.azurewebsites.net
http://127.0.0.1:5000/





