### steps to configure prometheus which scrape metrics from the online targets

## step1:
install promethues on VM
```bash
wget https://github.com/prometheus/prometheus/releases/latest/download/prometheus-*.linux-amd64.tar.gz
tar xvf prometheus-*.tar.gz
cd prometheus-*.linux-amd64
./prometheus

```
## step 2:
in this step we will configure promethus ,what target to scrape metrics from
in the binary change prometheus .yml file with the targets you want to scrape

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'my-app'
    static_configs:
      - targets:
          -demo.promlabs.com:10000
    
  - job_name: 'demo'
    static_configs:
      - targets:
           -localhost:9090

 ##  by this configuration prometheus will scrape metrics from two endpoint one is prometheus itself and the other one is public instances this file stores in the location --config.file and the metrics data will store into location(--storage.tsdb.path=data)         
```
## step3:
prometheus does not give alerts directly, it give alerts to alertmanager and alertmanager give the message to adimistrator or the person who is responsible, in this example i take a demo target if the instance shutdown for more than 2 minutes it will give allert to my email
to do this we have to change prometheus.yml file with adding some rules
```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'my-app'
    static_configs:
      - targets:
          -demo.promlabs.com:10000
    
  - job_name: 'demo'
    static_configs:
      - targets:
           -localhost:9090
rules_files :
     - "alerts.yaml"
 


---
create a seprate yaml defining the alerts rules named by alerts.yaml with below configufration
groups:
  - name: example-alerts
    rules:
      - alert: AppDown
        expr: up{job="demo"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "App is down"
          description: "The application has been down for more than 1 minute."

```
reload the prometheus server
## step4:
download alert maanger:
``` bash
wget https://github.com/prometheus/alertmanager/releases/latest/download/alertmanager-*.tar.gz
```
create config:create a config file named by alertmanager with this configuration
```yaml
global:
  resolve_timeout: 5m

route:
  receiver: 'email-notification'

receivers:
  - name: 'email-notification'
    email_configs:
      - to: 'ssuryanshijain3015@gmail.com'
        from: 'alertmanager@example.com'
        smarthost: 'smtp.gmail.com:587'
        auth_username: 'your_email@example.com'
        auth_identity: 'your_email@example.com'
        auth_password: 'your_email_app_password'
```
start alert manager:
```bash
./alertmanager --config.file=alertmanager.yml
```
## step5:
add this configration in promethus.yml and restart the server
```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - 'localhost:9093'  # AlertManager's port
```
all the setup is done .
in the end add grafana dashboard to it by providing the source as promethues demo 

 ## screenshots :(images)


