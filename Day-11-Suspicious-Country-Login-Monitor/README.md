# Day 11 – Suspicious Country Login Monitor

## Overview

The Suspicious Country Login Monitor is a beginner-friendly Python project that simulates basic geographical login activity monitoring.

The program maintains a predefined list of countries and analyses each country using conditional statements.

It classifies login activity into three categories:

- Normal Activity
- High-Risk Login
- Review Login Activity

This project demonstrates how Python lists, loops, and conditional statements can be combined to implement basic security monitoring logic.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python lists and loops.
- Practise `if`, `elif`, and `else` statements.
- Analyse login activity based on country.
- Classify login activity into security categories.
- Generate security monitoring reports.
- Understand basic authentication security concepts.

## Monitoring Logic

The program classifies countries using predefined conditions.

| Country | Security Classification |
|---|---|
| India | Normal Activity |
| China | High Risk Login |
| Russia | High Risk Login |
| Canada | Normal Activity |
| Ukraine | Review Login Activity |
| Nigeria | Review Login Activity |

## Structure

```
Day-11-Suspicious-Country-Login-Monitor/
│
├── country_login_monitor.py
├── README.md
│
└── screenshots/
    ├── country-login-monitor-code.png
    └── country-login-monitor-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-11-Suspicious-Country-Login-Monitor
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Execute the Python program

```
python3 country_login_monitor.py
```

## Sample Output

```
--- LOGIN MONITOR REPORT ---

Normal activity: India
HIGH RISK LOGIN: China
HIGH RISK LOGIN: Russia
Normal activity: Canada
Review login activity from: Ukraine
Review login activity from: Nigeria
```

## Skills Demonstrated

- Python lists
- Python `for` loops
- Conditional statements
- Logical operators (`or`)
- Country-based classification logic
- Security alert generation
- Basic authentication monitoring concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python conditional statements and logical operators can be used to classify login activity based on predefined country rules.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Important Security Note

This project is an educational simulation. It uses manually defined country classifications and does not identify actual malicious users or monitor real authentication events.

Country alone is not reliable evidence of a malicious login. Real security systems should consider additional signals such as unfamiliar devices, impossible travel, IP reputation, unusual access patterns, and multi-factor authentication.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 11
