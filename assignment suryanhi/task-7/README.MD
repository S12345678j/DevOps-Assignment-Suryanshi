#  Backup & Disaster Recovery Strategy – Enterprise Application on Azure
 the backup and disaster recovery strategy for an enterprise application deployed on Microsoft Azure. It includes defined RTO/RPO, automated backup examples, and infrastructure considerations.

---

## Overview

Ensuring business continuity and data protection is critical for modern cloud applications. This strategy leverages Azure-native tools to minimize data loss and reduce downtime during failures or disasters.

---

## Objectives

- **RTO (Recovery Time Objective)**: 30 minutes for critical services
- **RPO (Recovery Point Objective)**: 5–15 minutes depending on component
- **Automated, geo-redundant backups**
- **Disaster simulation and restore testing**
- **Immutable backup storage and deletion protection**

---

##  Architecture

| Component        | Azure Service           | Backup Strategy                   |
|------------------|-------------------------|------------------------------------|
| App Layer        | Azure VM / App Service  | VM Snapshot / Redeploy from Git   |
| Database Layer   | Azure PostgreSQL        | Automated Backups (up to 35 days) |
| Object Storage   | Azure Blob Storage      | RA-GRS Replication + Soft Delete  |

---

## RTO & RPO Targets

| Component        | RTO     | RPO     |
|------------------|---------|---------|
| PostgreSQL DB    | 15 mins | 5 mins  |
| Azure VM         | 30 mins | 15 mins |
| Blob Storage     | 30 mins | 15 mins |

---

## Backup Implementation

###  Azure PostgreSQL Flexible Server

- Automated backups (enabled by default)
- Extendable retention (up to 35 days)
- Geo-redundant backup storage

```bash
az postgres flexible-server update \
  --name <db-name> \
  --resource-group <resource-group> \
  --backup-retention 30
```
after completing this go to azure vm and perform following operations
Create a Recovery Services Vault

Go to Backup Center > + Backup

Choose:

Datasource Type: Azure VM

Policy: Daily at 2 AM, 30 days retention

Enable Instant Restore

