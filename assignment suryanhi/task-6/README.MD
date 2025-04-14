### This Bash script automates the setup of a basic web server on an Ubuntu machine. Here's what it does step-by-step:

## step1:
Updates the list of available packages.
Installs the latest versions of all packages.

## atep2:
Installs useful command-line tools: curl, wget, and git.

## step3:
Installs the NGINX web server.
Starts the NGINX service.
Enables it to start on boot.

## step4:
Configures the firewall (UFW) to  allow HTTP (port 80) traffic.
Enables the firewall.

## step5:
Creates a simple HTML file at /var/www/html/index.html which NGINX serves by default.

The page says: “Hello, World! Our server setup is complete!”
 
### How to Run This Script
- Save the script as script.sh
- Make it executable:
```bash
   chmod +x script.sh
```

- Run the script:
```bash
./ script.sh
``` 
 

 
