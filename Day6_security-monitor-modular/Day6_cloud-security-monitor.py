# Cloud Security Monitor

A Python-based cloud security monitoring project that analyses failed login attempts, identifies risk levels, and recommends security actions for administrators and standard users.

## Project Overview

This project simulates a cloud security monitoring system used by security teams to detect suspicious login activity.

The application evaluates failed login attempts and categorises accounts into different security risk levels.

Based on the detected risk, the system recommends security actions such as monitoring, investigation, or account lockdown.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Modular Python design
- Functions and Imports
- Security Risk Analysis
- Failed Login Monitoring
- Administrator Detection
- Security Incident Classification
- Automated Security Recommendations
```

## Module: security_utils.py

```
def check_login_risk(failed_logins):

    if failed_logins >= 15:
        return "ACCOUNT LOCKED"

    elif failed_logins >= 10:
        return "CRITICAL ALERT"

    elif failed_logins >= 5:
        return "WARNING"

    else:
        return "SAFE"
```

## Main Program: cloud_security_monitor.py

```
from security_utils import check_login_risk

username = input("Enter Username: ")
failed_logins = int(input("Enter Failed Login Attempts: "))
is_admin = input("Is this an Admin Account? (Yes/No): ")

risk = check_login_risk(failed_logins)

print("\n--- CLOUD SECURITY REPORT ---")
print("Username:", username)
print("Risk Level:", risk)
```

## Sample Output

### Account Locked

```
Enter Username: Sri
Enter Failed Login Attempts: 16
Is this an Admin Account? (Yes/No): No

--- CLOUD SECURITY REPORT ---
Username: Sri
Risk Level: ACCOUNT LOCKED
Account Type: Standard User
Action: Lock the Account Immediately
```

### Critical Alert

```
Enter Username: Gayathri
Enter Failed Login Attempts: 12
Is this an Admin Account? (Yes/No): No

--- CLOUD SECURITY REPORT ---
Username: Gayathri
Risk Level: CRITICAL ALERT
Account Type: Standard User
Action: Disable Account and Investigate
```

### Warning

```
Enter Username: sri gayathri
Enter Failed Login Attempts: 9
Is this an Admin Account? (Yes/No): Yes

--- CLOUD SECURITY REPORT ---
Username: sri gayathri
Risk Level: WARNING
Account Type: Administrator
Action: Monitor User Activity
```

### Safe

```
Enter Username: Sri Gayathri
Enter Failed Login Attempts: 2
Is this an Admin Account? (Yes/No): Yes

--- CLOUD SECURITY REPORT ---
Username: Sri Gayathri
Risk Level: SAFE
Account Type: Administrator
Action: No Threat Detected
```

## Security Risk Levels

| Failed Attempts | Risk Level |
|---------------|------------|
| 0 - 4 | SAFE |
| 5 - 9 | WARNING |
| 10 - 14 | CRITICAL ALERT |
| 15+ | ACCOUNT LOCKED |

## Learning Objectives

This project helped me practice:

- Python Functions
- Modules and Imports
- Conditional Statements
- User Input Validation
- Security Monitoring Logic
- Incident Response Concepts
- Access and Risk Management

## Cybersecurity Relevance

This project introduces concepts commonly used in:

- Security Operations Centres (SOC)
- Cloud Security Monitoring
- SIEM Platforms
- Identity and Access Management (IAM)
- Incident Detection and Response
- Security Alerting Systems

Monitoring failed login attempts is an important security practice used to identify brute-force attacks, credential stuffing attacks, and unauthorised access attempts.

## Skills Demonstrated

- Python Programming
- Modular Development
- Security Monitoring
- Risk Assessment
- Security Automation
- Incident Response Logic
- Cloud Security Fundamentals


## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
