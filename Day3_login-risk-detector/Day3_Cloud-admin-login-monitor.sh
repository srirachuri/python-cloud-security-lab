# Cloud Admin Login Monitor

## Overview

Cloud Admin Login Monitor is a Python-based cybersecurity project that analyses login activity and identifies potential security risks based on failed login attempts and account privilege levels.

The tool simulates how cloud security teams monitor privileged account activity and detect suspicious authentication events before they become security incidents.

---

## Features

- Username monitoring
- Failed login attempt analysis
- Security risk classification
- Account lockout detection
- Privileged account identification
- Cloud security reporting
- Admin account monitoring

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Virtual Environment (venv)
- Nano Editor

---

## Security Classification Logic

| Failed Attempts | Status |
|---------------|---------|
| 0 – 4 | SAFE |
| 5 – 9 | WARNING |
| 10 – 14 | CRITICAL ALERT |
| 15+ | ACCOUNT LOCKED |

---

## Privileged Account Monitoring

The program checks whether the login belongs to:

- Standard User
- Privileged Administrator

Administrator accounts receive additional monitoring because they have elevated access to cloud resources.

---

## Running the Program

```
python3 cloud_login_monitor.py
```

---

## Sample Output

### Account Locked

```
Enter username: Sri Gayathri
Enter failed login attempts: 15
Is this an Admin? (Yes/no): no

---CLOUD SECURITY REPORT---

ACCOUNT LOCKED
Standard User
```

### Warning

```
Enter username: Sri Gayathri
Enter failed login attempts: 6
Is this an Admin? (Yes/no): no

---CLOUD SECURITY REPORT---

WARNING
Standard User
```

### Critical Alert

```
Enter username: Sri Gayathri
Enter failed login attempts: 12
Is this an Admin? (Yes/no): Yes

---CLOUD SECURITY REPORT---

CRITICAL ALERT
Privileged Account Detected
```

### Safe Activity

```
Enter username: Sri Gayathri
Enter failed login attempts: 3
Is this an Admin? (Yes/no): Yes

---CLOUD SECURITY REPORT---

SAFE
Privileged Account Detected
```

---

## Skills Demonstrated

- Python Variables
- User Input Handling
- Conditional Statements
- Security Monitoring
- Cloud Security Fundamentals
- Authentication Analysis
- Risk Classification
- Privileged Access Monitoring

---

## Cloud Security Relevance

This project demonstrates concepts commonly used in:

- Cloud Security Operations (Cloud SOC)
- Identity and Access Management (IAM)
- Privileged Access Management (PAM)
- Security Monitoring
- Threat Detection
- Incident Response
- Zero Trust Security

Cloud administrators are high-value targets because they have access to critical infrastructure. Monitoring administrator login activity is an essential cloud security control.

---

## Learning Outcomes

Through this project, I practised:

- Python programming
- Authentication security concepts
- Privileged account monitoring
- Cloud security fundamentals
- Risk assessment
- Security reporting
- Linux command-line development

---

## Author

Sri Gayathri

Aspiring Cloud Security Engineer

Current Learning Focus:
- Python for Cybersecurity
- Linux Administration
- Networking Fundamentals
- AWS Security
- Azure Security
- Security Operations (SOC)
