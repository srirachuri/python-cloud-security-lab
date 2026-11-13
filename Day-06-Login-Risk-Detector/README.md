# Day 6 – Login Risk Detector

## Overview

The Login Risk Detector is a beginner-friendly Python project that simulates basic login security monitoring.

The program analyses failed login attempts, identifies suspicious authentication activity, detects potential brute-force attacks, and classifies account types as Administrator or Standard User.

This project demonstrates how Python conditional statements can be used to implement basic security monitoring and threat detection logic.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Understand Python conditional statements.
- Analyse failed login attempts.
- Detect potential brute-force attacks.
- Identify suspicious login activity.
- Classify login risk levels.
- Identify administrator and standard user accounts.
- Practice basic security automation concepts.

## Detection Logic

| Failed Login Attempts | Security Classification |
|---|---|
| 0–4 | SAFE – Normal Activity |
| 5–9 | WARNING – Suspicious Login Attack |
| 10 or more | CRITICAL ALERT – Brute Force Attack Detected |

The program also identifies whether the account belongs to an Administrator or Standard User.

## Structure

```
Day-06-Login-Risk-Detector/
│
├── login_risk_detector.py
├── README.md
│
└── screenshots/
    ├── login-risk-detector-code.png
    └── login-risk-detector-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project folder

```
cd cloud-security-projects/Day-06-Login-Risk-Detector
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Run the program

```
python login_risk_detector.py
```

## Sample Output

### Test 1 – Critical Alert

```
Enter username: Sri Gayathri
Enter failed login attempts: 19

--- SECURITY ANALYSIS---
CRITICAL ALERT: Brute Force Attack Detected!
Account Type: Administrator
```

### Test 2 – Warning

```
Enter username: SRI GAYATHRI
Enter failed login attempts: 9

--- SECURITY ANALYSIS---
WARNING: SUSPICIOUS Login Attack
Account Type: Administrator
```

### Test 3 – Safe Activity

```
Enter username: sri gayathri
Enter failed login attempts: 3

--- SECURITY ANALYSIS---
SAFE: Normal Activity
Account Type: Administrator
```

## Skills Demonstrated

- Python programming fundamentals
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Login risk classification
- Brute-force attack detection concepts
- Basic authentication security
- Privileged account identification
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python can be used to simulate login security monitoring, classify authentication risks, and identify potential brute-force attacks.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This project is an educational simulation. It uses manually entered login information and does not monitor actual authentication logs, connect to cloud identity providers, or automatically block accounts.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 6
