# Day 5 – Cloud Admin Login Monitor

## Project Overview

The Cloud Admin Login Monitor is a beginner-friendly Python project designed to simulate basic cloud account security monitoring.

The program analyses user-provided login information, checks failed login attempts, identifies potentially suspicious activity, and detects privileged administrator accounts.

This project demonstrates how Python conditional statements can be used to implement basic security monitoring logic.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- VS Code / GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Understand Python conditional statements (`if`, `elif`, `else`).
- Identify suspicious login activity.
- Detect excessive failed login attempts.
- Generate security alerts based on failed login thresholds.
- Identify privileged administrator accounts.
- Practice basic security automation concepts.

## Security Monitoring Logic

| Failed Login Attempts | Security Status |
|---|---|
| 0–4 | SAFE |
| 5–9 | WARNING |
| 10–14 | CRITICAL ALERT |
| 15 or more | ACCOUNT LOCKED |

The program also checks whether the account is an administrator or a standard user.

## Project Structure

```
Day-05-Cloud-Admin-Login-Monitor/
│
├── cloud_admin_login_monitor.py
├── README.md
│
└── screenshots/
    ├── cloud-admin-login-monitor-code.png
    └── cloud-admin-login-monitor-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-05-Cloud-Admin-Login-Monitor
```

### Step 3: Activate your virtual environment (if available)

```
source venv/bin/activate
```

### Step 4: Run the Python script

```
python3 cloud_admin_login_monitor.py
```

## Sample Output

```
Enter username: Sri Gayathri
Enter failed login attempts: 15
Is this an Admin? (Yes/no): no

---CLOUD SECURITY REPORT---
ACCOUNT LOCKED
Standard User
```

Other test scenarios:

- 6 failed attempts → WARNING
- 12 failed attempts → CRITICAL ALERT
- 3 failed attempts → SAFE
- Administrator account → Privileged Account Detected

## Skills Demonstrated

- Python programming fundamentals
- Conditional statements
- User input handling
- Security alert classification
- Privileged account identification
- Basic cloud security concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python can be used to implement basic security monitoring logic, classify suspicious login activity, and identify privileged accounts.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. It accepts manually entered information and does not connect to real cloud authentication systems, monitor actual login logs, or automatically lock user accounts.

---

**Author:** Sri Gayathri Rachuri  
**Project:** Python for Cloud Security – Day 5
