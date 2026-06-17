# Login Risk Detector

## Overview

Login Risk Detector is a Python-based cybersecurity project that analyzes login attempts and classifies account activity based on the number of failed login attempts.

The program simulates a Security Operations Center (SOC) workflow by identifying suspicious login behavior, brute-force attacks, and administrator account activity.

---

## Features

- Username monitoring
- Failed login analysis
- Risk-based alert generation
- Brute-force attack detection
- Administrator account identification
- Security report generation

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Virtual Environment (venv)
- Nano Text Editor

---

## Security Logic

The application evaluates login risk using failed login attempts.

| Failed Attempts | Risk Level |
|---------------|------------|
| 0 - 4 | Safe |
| 5 - 9 | Warning |
| 10+ | Critical |

---

## Detection Rules

### Safe Activity

```
SAFE: Normal Activity
```

Triggered when failed login attempts are less than 5.

---

### Suspicious Activity

```
WARNING: SUSPICIOUS Login Attack
```

Triggered when failed login attempts are between 5 and 9.

---

### Critical Alert

```text
CRITICAL ALERT: Brute Force Attack Detected!
```

Triggered when failed login attempts are 10 or higher.

---

## Administrator Monitoring

The program identifies privileged accounts:

```
Account Type: Administrator
```

Monitoring administrator accounts is important because they have elevated permissions and are often targeted by attackers.

---

## Running the Program

```
python3 login_risk_detector.py
```

---

## Example Output

### Critical Risk

```text
Enter username: Sri Gayathri
Enter failed logins attempts: 19

--- SECURITY ANALYSIS ---

CRITICAL ALERT: Brute Force Attack Detected!
Account Type: Administrator
```

### Medium Risk

```
Enter username: Sri Gayathri
Enter failed logins attempts: 9

--- SECURITY ANALYSIS ---

WARNING: SUSPICIOUS Login Attack
Account Type: Administrator
```

### Normal Activity

```text
Enter username: Sri Gayathri
Enter failed logins attempts: 3

--- SECURITY ANALYSIS ---

SAFE: Normal Activity
Account Type: Administrator
```

---

## Skills Demonstrated

- Python Variables
- User Input Handling
- Conditional Statements
- Security Monitoring
- Risk Classification
- Brute Force Detection
- SOC Fundamentals
- Linux Command Line

---

## Cybersecurity Relevance

This project demonstrates concepts commonly used in:

- Security Operations Centers (SOC)
- Identity and Access Management (IAM)
- Threat Detection
- Brute Force Monitoring
- Incident Response
- User Behavior Analysis

Organizations use similar logic to detect abnormal login behavior and reduce unauthorized access attempts.

---

## Learning Outcomes

Through this project I practiced:

- Python programming
- Login risk analysis
- Security monitoring concepts
- Threat detection logic
- Cybersecurity fundamentals
- Linux-based development

---

## Author

Sri Gayathri

Aspiring Cloud Security Engineer

Learning Path:
- Python for Cybersecurity
- Linux Administration
- Networking Fundamentals
- AWS Cloud Security
- SOC Operations
