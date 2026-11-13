# Day 14 – Cloud Security Monitor Using Python

## Overview

The Cloud Security Monitor is a beginner-friendly Python project that simulates basic cloud account security monitoring.

The program analyses login activity using failed login attempts and administrator account status.

It uses a separate Python utility module to classify login risk and generates a security report containing:

- Username
- Risk Level
- Account Type
- Recommended Security Action

This project demonstrates Python functions, modules, imports, conditional statements, and reusable security logic.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python modules.
- Practise importing functions from another Python file.
- Create reusable security utility functions.
- Analyse failed login attempts.
- Identify administrator accounts.
- Classify login risk levels.
- Generate security reports.
- Understand basic cloud security monitoring concepts.

## Project Architecture

The project contains two Python modules.

### 1. security_utils.py

Responsible for:

- Defining the `check_login_risk()` function.
- Analysing failed login attempts.
- Returning the appropriate risk classification.

### 2. cloud_security_monitor.py

Responsible for:

- Collecting username and login information.
- Importing the security utility function.
- Identifying account type.
- Generating security reports.
- Recommending security actions.

## Security Classification Logic

| Failed Login Attempts | Risk Level |
|---|---|
| 0–4 | SAFE |
| 5–9 | WARNING |
| 10–14 | CRITICAL ALERT |
| 15 or more | ACCOUNT LOCKED |

The program also identifies administrator accounts and displays additional security recommendations for privileged accounts.

## Project Structure

```
Day-14-Cloud-Security-Monitor/
│
├── cloud_security_monitor.py
├── security_utils.py
├── README.md
│
└── screenshots/
    ├── security-utils-code.png
    ├── cloud-security-monitor-code.png
    ├── cloud-security-monitor-output-1.png
    └── cloud-security-monitor-output-2.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-14-Cloud-Security-Monitor
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Run the main program

```
python3 cloud_security_monitor.py
```

**Important:** Keep both Python files in the same directory so the main program can import `security_utils.py`.

## Sample Output

### Test 1 – Account Locked

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

### Test 2 – Critical Alert

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

### Test 3 – Warning

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

### Test 4 – Safe

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

## Skills Demonstrated

- Python functions
- Python modules
- Import statements
- Code reusability
- Conditional statements
- Function parameters and return values
- User input handling
- Authentication risk classification
- Security report generation
- Basic cloud security automation concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how to organise Python programs into separate modules and reuse functions across files.

I also practised building a basic cloud security monitoring workflow that analyses login activity, identifies account types, classifies risk levels, and recommends security actions.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. It uses manually entered login information and does not connect to real cloud identity providers, automatically lock accounts, or monitor actual authentication events.

The security actions are recommendations displayed by the program, not actions performed on real accounts.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 14
