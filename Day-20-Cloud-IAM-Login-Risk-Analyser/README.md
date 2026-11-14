# Day 20 – Cloud IAM Login Risk Analyser Using Python

## Overview

This project demonstrates a Python-based Cloud IAM Login Risk Analyser designed to identify suspicious cloud login activity using JSON data.

### Scenario

Working as a Junior Cloud Security Analyst, a SIEM system receives a JSON file containing cloud login information.

The task is to analyse the login details, identify suspicious activity, determine the risk level, generate a security report, and recommend appropriate security actions.

## Learning Objectives

- Read JSON files using Python.
- Analyse cloud login information.
- Detect suspicious login activity.
- Identify failed login attempts.
- Detect administrator accounts.
- Check Multi-Factor Authentication (MFA) status.
- Identify foreign login activity.
- Detect high-risk administrator accounts without MFA.
- Assign security risk levels.
- Recommend security response actions.

## Technologies Used

- Python 3
- JSON
- Linux
- AWS Cloud Security concepts
- VS Code
- Git and GitHub

## Project Structure

```
Day-20-Cloud-IAM-Login-Risk-Analyser/
│
├── README.md
├── iam_login.json
├── iam_login_analyzer.py
└── screenshots/
```

## Practical Implementation

### 1. Create IAM Login JSON File

Created `iam_login.json` containing sample cloud authentication information.

Example:

```
{
    "username": "cloud-admin",
    "cloud_provider": "AWS",
    "country": "Russia",
    "failed_logins": 11,
    "is_admin": true,
    "mfa_enabled": false,
    "ip_address": "203.0.113.25"
}
```

### 2. Python IAM Login Analyser

Created `iam_login_analyzer.py` to read and analyse the JSON login information.

The program extracts:

- Username
- Cloud provider
- IP address
- Country
- Failed login attempts
- Administrator account status
- MFA status

### 3. Risk Level Detection

The program assigns a risk level based on failed login attempts.

| Failed Login Attempts | Risk Level |
|---|---|
| 0–4 | SAFE |
| 5–9 | WARNING |
| 10 or more | CRITICAL |

### 4. Suspicious Activity Detection

The analyser checks for the following security conditions:

| Security Check | Detection |
|---|---|
| Failed Logins | Identifies excessive failed attempts |
| Administrator Account | Detects administrator privileges |
| MFA Status | Identifies disabled MFA |
| Foreign Login | Detects login activity outside India |
| High-Risk Admin | Detects administrator accounts without MFA |

### 5. Security Alerts

The program generates alerts for:

- Multi-Factor Authentication being disabled.
- Foreign login activity.
- Administrator accounts operating without MFA.

### 6. Recommended Security Actions

Based on the assigned risk level, the program recommends security actions.

**CRITICAL Risk**
- Lock the account.
- Investigate login activity.
- Reset user password.
- Review CloudTrail/Audit logs.

**WARNING Risk**
- Monitor user activity.
- Enable MFA.
- Review recent login history.

**SAFE Risk**
- No immediate action required.

## Expected Output

Using the sample JSON data:

```
========== CLOUD SECURITY REPORT ==========

Username       : cloud-admin
Cloud Provider : AWS
IP Address     : 203.0.113.25
Country        : Russia
Failed Logins  : 11

Risk Level : CRITICAL
Account Type : Administrator
ALERT        : Multi-Factor Authentication is DISABLED
ALERT        : Foreign login detected
CRITICAL     : Admin account without MFA

========== RECOMMENDED ACTION ==========

- Lock the account
- Investigate login activity
- Reset user password
- Review CloudTrail/Audit logs
```

## How to Run the Project

### Step 1: Activate Virtual Environment

```
source venv/bin/activate
```

### Step 2: Run the Python Program

```
python3 iam_login_analyzer.py
```

## Python Concepts Practised

| Concept | Purpose |
|---|---|
| `import json` | Import JSON module |
| `json.load()` | Read JSON data |
| `with open()` | Safely open files |
| `if-elif-else` | Risk classification |
| Boolean conditions | Check administrator and MFA status |
| Logical operators | Detect combined security risks |
| `print()` | Generate security reports |

## Learning Outcomes

Successfully practised Python JSON handling, cloud IAM login analysis, suspicious activity detection, administrator account monitoring, MFA verification, foreign login detection, security risk classification, and automated security recommendations.

## Project Status

**Completed – Day 20 of the Python Cloud Security Learning Roadmap.**

Next: Continue Python for Cloud Security with more practical security automation exercises.
