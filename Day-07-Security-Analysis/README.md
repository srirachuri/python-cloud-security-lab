# Day 7 – Security Analysis Using Python

## Overview

This project is a beginner-friendly Python-based security analysis program designed to simulate basic login security monitoring.

The program accepts a username and the number of failed login attempts, analyses the activity, and generates a security status based on predefined thresholds.

It identifies potentially suspicious authentication activity and classifies login attempts into different security levels.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Practice Python conditional statements.
- Analyse failed login attempts.
- Identify potentially suspicious login activity.
- Classify security risk levels.
- Understand basic authentication monitoring.
- Develop foundational Python security automation skills.

## Security Classification Logic

| Failed Login Attempts | Security Status |
|---|---|
| 0–4 | SAFE |
| 5–9 | WARNING |
| 10–14 | CRITICAL ALERT |
| 15 or more | ACCOUNT LOCKED |

## Structure

```
Day-07-Security-Analysis/
│
├── security_analysis.py
├── README.md
│
└── screenshots/
    ├── security-analysis-code.png
    └── security-analysis-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-07-Security-Analysis
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Execute the Python program

```
python3 security_analysis.py
```

## Sample Output

### Test 1 – Account Locked

```
Enter username: Sri Gayathri
Enter Failed Login Attempts: 18

---SECURITY ANALYSIS---
ACCOUNT LOCKED
```

### Test 2 – Warning

```
Enter username: SRI GAYATHRI
Enter Failed Login Attempts: 9

---SECURITY ANALYSIS---
WARNING
```

### Test 3 – Safe

```
Enter username: sri gayathri
Enter Failed Login Attempts: 3

---SECURITY ANALYSIS---
SAFE
```

## Skills Demonstrated

- Python fundamentals
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Authentication risk classification
- Security monitoring concepts
- Linux command-line operations
- Basic security automation

## Learning Outcome

Through this project, I practised implementing security classification logic using Python.

I learned how conditional statements can be used to analyse failed login attempts and generate security alerts based on predefined thresholds.

This project is part of my Python learning roadmap focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. It uses manually entered login information and does not monitor real authentication logs, integrate with cloud identity providers, or automatically lock user accounts.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 7
