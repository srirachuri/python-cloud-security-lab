# Day 12 – Login Risk Analyser Using Python

## Overview

The Login Risk Analyser is a beginner-friendly Python security monitoring project designed to simulate authentication risk analysis.

The program accepts a username, the number of failed login attempts, and the administrator account status.

It uses a reusable Python function to analyse login activity, classify security risks, and recommend appropriate security response actions.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python functions.
- Practise function parameters and arguments.
- Analyse failed login attempts.
- Identify potentially suspicious authentication activity.
- Classify login risk levels.
- Generate security response recommendations.
- Understand basic cloud account security concepts.

## Security Analysis Logic

| Condition | Risk Level | Recommended Action |
|---|---|---|
| 15 or more failed attempts | ACCOUNT LOCKED | Disable account and investigate immediately |
| 10 or more attempts on an administrator account | HIGH PRIORITY SECURITY INCIDENT | Investigate administrator account |
| 10–14 attempts | CRITICAL INCIDENT | Investigate possible brute-force attack |
| 5–9 attempts | WARNING | Monitor user activity |
| 0–4 attempts | SAFE | No immediate threat |

## Project Structure

```
Day-12-Login-Risk-Analyser/
│
├── login_monitor.py
├── README.md
│
└── screenshots/
    ├── login-risk-analyser-code.png
    └── login-risk-analyser-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-12-Login-Risk-Analyser
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Execute the Python program

```
python3 login_monitor.py
```

## Sample Output

### Test 1 – Account Locked

```
Enter Username: sri gayathri
Enter Failed Login Attempts: 22
Is this an Admin Account? (Yes/No): No

--- SECURITY REPORT ---
Username: sri gayathri
Risk Level: ACCOUNT LOCKED
Action: Disable Account and Investigate Immediately
```

### Test 2 – Warning

```
Enter Username: SRI GAYATHRI
Enter Failed Login Attempts: 9
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---
Username: SRI GAYATHRI
Risk Level: WARNING
Action: Monitor User Activity
```

### Test 3 – Safe

```
Enter Username: Sri Gayathri
Enter Failed Login Attempts: 3
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---
Username: Sri Gayathri
Risk Level: SAFE
Action: No Immediate Threat
```

## Skills Demonstrated

- Python functions
- Function parameters and arguments
- Conditional statements (`if`, `elif`, `else`)
- Logical operators (`and`)
- User input handling
- Authentication risk classification
- Security response recommendations
- Basic security automation concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python functions can organise reusable security analysis logic.

I practised analysing login attempts, identifying potential authentication risks, and recommending security response actions based on predefined conditions.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. It uses manually entered login information and does not connect to actual cloud authentication systems, automatically disable accounts, or monitor real login events.

The security actions are recommendations printed by the program, not actions performed on real accounts.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 12
