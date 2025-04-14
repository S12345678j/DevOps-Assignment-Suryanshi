### gitlab file for automated the deployment process
In the stages section i define the order of the jobs(build and deploy) first build stage will execute and after that deploy stage will execute if build stage fails deploy stage will never be executed.

I make global veriables to access in the build job and deploy job ,zip file contains the application code and other variables as they required .

In the before script section i write 5 commands to install azure cli on vm and login into azure with my user credentials.

I provide my user credentials as secrets so that noone can access them.

This gitlab file have two jobs, build and deploy :
in the before script section i write 5 commands to install azure cli on vm and login into azure with my user credentials.
 
## build :
in the build section pip install command will install all the dependencies to run the application and unzip the application code 


## deploy :
the deploy stage automates the process of creating Azure infrastructure and deploying your Python web app to Azure App Service
in the deploy section there are 4 steps to deploy the app:
step1:create resource group
step2:create app service plan
step3:create web app
step4:deploy the application


