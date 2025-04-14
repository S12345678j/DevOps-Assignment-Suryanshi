#!/bin/bash

# Update package repository and system
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install essential tools
echo "Installing essential tools..."
sudo apt install -y curl wget git

# Install NGINX web server
echo "Installing NGINX web server..."
sudo apt install -y nginx

# Start NGINX service
echo "Starting NGINX..."
sudo systemctl start nginx
sudo systemctl enable nginx

# Configure firewall to allow HTTP traffic
echo "Configuring firewall for HTTP traffic..."
sudo ufw allow 'Nginx HTTP'
sudo ufw enable

# Create a sample HTML file
echo "Creating a sample webpage..."
echo "<html>
<head>
    <title>Welcome!</title>
</head>
<body>
    <h1>Hello, World! Our server setup is complete!</h1>
</body>
</html>" | sudo tee /var/www/html/index.html

# Print server details
echo "Setup complete. Server is running!"
echo "Visit your server's public IP to see the webpage."