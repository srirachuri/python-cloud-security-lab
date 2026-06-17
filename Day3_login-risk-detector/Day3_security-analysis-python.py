# Security Analysis Python

## Overview

Security Analysis Python is a beginner-friendly cybersecurity project that evaluates login activity based on failed login attempts and classifies the security risk level.

The program simulates how Security Operations Centre (SOC) teams analyse authentication events to identify suspicious behaviour, brute-force attacks, and account lockout situations.

---

## Features

- Username monitoring
- Failed login analysis
- Risk classification
- Account lockout detection
- Security alert generation
- SOC-style security reporting

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Virtual Environment (venv)
- Nano Text Editor

---

## Security Logic

The application classifies risk based on failed login attempts.

| Failed Login Attempts | Result |
|----------------------|----------|
| 0 - 4 | SAFE |
| 5 - 9 | WARNING |
| 10 - 14 | CRITICAL ALERT |
| 15+ | ACCOUNT LOCKED |

---

## Detection Rules

### Safe Activity

```
SAFE
```

User activity appears normal.

---

### Warning

```
WARNING
```

Suspicious login activity detected.

---

### Critical Alert

```
CRITICAL ALERT
```

Potential brute-force attack detected.

---

### Account Lockout

```
ACCOUNT LOCKED
```

Too many failed login attempts. Account access is disabled to prevent unauthorized access.

---

## Running the Program

```
python3 security_analysis.py
```

---

## Sample Output

### Account Locked

```
Enter username: Sri Gayathri
Enter Failed Login Attempts: 18

---SECURITY ANALYSIS---

ACCOUNT LOCKED
```

### Warning

```
Enter username: Sri Gayathri
Enter Failed Login Attempts: 9

---SECURITY ANALYSIS---

WARNING
```

### Safe

```
Enter username: Sri Gayathri
Enter Failed Login Attempts: 3

---SECURITY ANALYSIS---

SAFE
```

---

## Skills Demonstrated

- Python Variables
- User Input Handling
- Conditional Statements
- Security Monitoring
- Authentication Analysis
- Risk Classification
- Account Lockout Logic
- Linux Command Line

---

## Cybersecurity Relevance

This project demonstrates security concepts used in:

- Security Operations Centres (SOC)
- Identity and Access Management (IAM)
- Authentication Monitoring
- Brute Force Detection
- Account Protection
- Incident Response

Many organisations automatically lock accounts after repeated failed login attempts to reduce unauthorised access risks.

---

## Learning Outcomes

Through this project, I practised:

- Python programming fundamentals
- Security monitoring concepts
- Authentication analysis
- Risk assessment techniques
- Threat detection logic
- Linux-based development

---

## Author

Sri Gayathri

Aspiring Cloud Security Engineer

Current Learning Focus:
- Python for Cybersecurity
- Linux Administration
- Networking Fundamentals
- AWS Cloud Security
- Security Operations (SOC)
