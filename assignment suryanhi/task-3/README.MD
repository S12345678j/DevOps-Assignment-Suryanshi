### Security & Compliance 

## Task:
 Identify three security risks in DevOps workflows and propose mitigation strategies that align with ISO 27001, GDPR, or SOC 2 compliance.

# 1 Uncontrolled Access to Code Repositories
Risk: Developers or third parties may have excessive or unnecessary access to source code repositories, risking unauthorized code changes or data exposure.


## Compliance Relevance:

ISO 27001: Access Control

SOC 2: Security Principle – Access Controls

GDPR: Security of Processing

## Mitigation Strategy:

Implement Role-Based Access Control (RBAC) and principle of least privilege.

Maintain audit logs of access and code changes.

Use multi-factor authentication (MFA) for access to repositories.

Regularly review and update access policies.
     
# 2. Lack of Security Testing in CI/CD Pipelines
Risk: Code is deployed without adequate testing for vulnerabilities, increasing the risk of deploying insecure applications.


## Compliance Relevance:

ISO 27001: System Acquisition, Development and Maintenance

SOC 2: Change Management

GDPR: Data Protection by Design and Default

## Mitigation Strategy:

Integrate automated security scanning tools (e.g., static code analysis, dependency scanning) into the CI/CD pipeline.

Enforce code review policies with security-focused checklists.

Adopt DevSecOps practices to shift security left in the development process.
     
# 3. Weak Authentication Mechanism:

Risk: Secrets (e.g., API keys, credentials) are exposed through logs, code, or configuration files.

## Compliance Relevance:

ISO 27001: Annex A.10 – Cryptography

SOC 2: Confidentiality and Security Principles

GDPR: Article 32 – Confidentiality and Integrity

 ## Mitigation Strategy:

Use secret management tools (e.g., AWS Secrets Manager, HashiCorp Vault).

Ensure encryption at rest and in transit for all sensitive data.

Set permissions to prevent secrets from being logged or accessed unnecessarily.