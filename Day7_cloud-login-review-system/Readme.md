# Cloud Login Review System

A Python-based security review system that analyses login attempts and classifies security risks based on failed login activity.

This project simulates how cloud security teams review login events and identify suspicious account behaviour.

---

## Project Overview

The Cloud Login Review System evaluates login attempts and categorises users into different risk levels.

The system helps identify:

- Safe Accounts
- Warning Level Accounts
- Critical Security Alerts
- Locked Accounts
- High Priority Security Incidents for Admin Users

---

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

---

## Features

- Function-Based Programming
- Conditional Logic
- User Input Handling
- Login Risk Assessment
- Admin Account Monitoring
- Security Incident Detection
- Cloud Security Concepts

---

## Python Function

```
def review_login_attempts(username, failed_attempts, is_admin):

    print("\n--- SECURITY REPORT ---")
    print("Username:", username)

    if failed_attempts >= 15:
        print("ACCOUNT LOCKED")

    elif 10 <= failed_attempts <= 14:
        print("CRITICAL ALERT")

    elif 5 <= failed_attempts <= 9:
        print("WARNING")

    else:
        print("SAFE")

    if is_admin and failed_attempts >= 10:
        print("HIGH PRIORITY INCIDENT")
```

---

## Sample Output

### Account Locked

```
Enter Username: Sri
Enter Failed Login Attempts: 15
Is this an Admin Account? (Yes/No): No

--- SECURITY REPORT ---
Username: Sri
ACCOUNT LOCKED
```

### Critical Alert

```
Enter Username: Gayathri
Enter Failed Login Attempts: 12
Is this an Admin Account? (Yes/No): No

--- SECURITY REPORT ---
Username: Gayathri
CRITICAL ALERT
```

### Warning

```
Enter Username: sri gayathri
Enter Failed Login Attempts: 9
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---
Username: sri gayathri
WARNING
```

### Safe

```
Enter Username: Sri Gayathri
Enter Failed Login Attempts: 3
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---
Username: Sri Gayathri
SAFE
```

### High Priority Incident

```
Enter Username: AdminUser
Enter Failed Login Attempts: 12
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---
Username: AdminUser
CRITICAL ALERT
HIGH PRIORITY INCIDENT
```

---

## Risk Classification

| Failed Attempts | Risk Level |
|---------------|------------|
| 0 - 4 | SAFE |
| 5 - 9 | WARNING |
| 10 - 14 | CRITICAL ALERT |
| 15+ | ACCOUNT LOCKED |

---

## Learning Objectives

This project helped me practice:

- Python Functions
- Conditional Statements
- Boolean Logic
- Security Monitoring Concepts
- Login Risk Assessment
- User Input Processing
- Cloud Security Fundamentals

---

## Cybersecurity Relevance

Login monitoring is an important security control used in:

- Cloud Security
- Identity and Access Management (IAM)
- Security Operations Centres (SOC)
- Threat Detection
- Incident Response
- Security Monitoring Platforms

Monitoring failed login attempts helps identify:

- Brute Force Attacks
- Unauthorised Access Attempts
- Account Compromise Risks
- Privileged Account Abuse

---

## Skills Demonstrated

- Python Programming
- Security Monitoring
- Risk Analysis
- Incident Detection
- Access Control Awareness
- Cloud Security Fundamentals


## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
