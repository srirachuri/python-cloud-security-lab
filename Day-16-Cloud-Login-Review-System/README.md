# Day 16 – Cloud Login Review System Using Python

## Overview

The Cloud Login Review System is a Python-based security monitoring simulation designed to evaluate login activity and identify potentially suspicious authentication behavior.

The program analyses failed login attempts, checks whether the account is an administrator account, and generates a security report based on predefined risk levels.

It demonstrates how basic security monitoring logic can help identify unusual login activity in cloud environments.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Understand Python functions.
- Practise conditional statements.
- Analyse failed login attempts.
- Identify suspicious login activity.
- Apply different security risk levels.
- Understand administrator account monitoring.
- Generate basic security reports.

## Project Features

### 1. Login Activity Analysis

Accepts the following inputs:

- Username
- Number of failed login attempts
- Administrator account status

### 2. Security Risk Classification

| Failed Login Attempts | Risk Classification |
|---|---|
| 15 or more | ACCOUNT LOCKED |
| 10–14 | CRITICAL ALERT |
| 5–9 | WARNING |
| 0–4 | SAFE |

### 3. Administrator Monitoring

The system checks whether an account is an administrator.

If an administrator account has 10 or more failed login attempts, it generates an additional:

**HIGH PRIORITY INCIDENT**

### 4. Security Report

The program displays:

- Username
- Login security status
- Additional administrator security alert when applicable

## Project Structure

```
Day-16-Cloud-Login-Review-System/
│
├── cloud_security_review.py
├── README.md
│
└── screenshots/
    ├── cloud-login-review-code.png
    └── cloud-login-review-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project folder

```
cd cloud-security-projects/Day-16-Cloud-Login-Review-System
```

### Step 3: Run the Python program

```
python3 cloud_security_review.py
```

## Sample Output

### Test 1 – Account Locked

```
--- SECURITY REPORT ---
Username: Sri
ACCOUNT LOCKED
```

### Test 2 – Critical Alert

```
--- SECURITY REPORT ---
Username: Gayathri
CRITICAL ALERT
```

### Test 3 – Warning

```
--- SECURITY REPORT ---
Username: sri gayathri
WARNING
```

### Test 4 – Safe Login Activity

```
--- SECURITY REPORT ---
Username: Sri Gayathri
SAFE
```

## Skills Demonstrated

- Python functions
- Function parameters
- Conditional statements
- Boolean logic
- User input handling
- String methods
- Security risk classification
- Basic authentication monitoring
- Linux command-line operations

## Learning Outcomes

Through this project, I learned how to implement login activity analysis using Python functions and conditional statements.

I also practised identifying suspicious authentication patterns and generating security alerts based on account type and failed login attempts.

This project is part of my Python learning journey focused on Cloud Support and Cloud Security.

## Security Disclaimer

This project is an educational simulation. It does not connect to real cloud authentication systems, lock actual user accounts, or automatically detect attacks.

Real-world implementations require integration with authentication logs, identity providers, monitoring systems, and appropriate incident-response controls.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 16
