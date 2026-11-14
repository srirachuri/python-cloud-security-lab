# Day 18 – Cloud Security Log Analyser Using Python

## Overview

This project demonstrates a practical Cloud Security Log Analyser developed using Python.

### Scenario

Working as a Junior Cloud Security Analyst, the task is to analyse company authentication logs, identify failed and successful login attempts, detect administrator and root login attempts, assign a risk level, and generate an automated security report.

## Objectives

- Read authentication log files using Python.
- Count failed login attempts.
- Count successful login attempts.
- Detect administrator login attempts.
- Detect root login attempts.
- Assign security risk levels.
- Generate automated security reports.
- Handle missing files using exception handling.

## Technologies Used

- Python 3
- Linux
- VS Code
- Git and GitHub

## Project Structure

```
Day-18-Cloud-Security-Log-Analyser/
│
├── README.md
├── auth.log
├── cloud_log_analyser.py
├── security_report.txt
└── screenshots/
```

## Practical Implementation

### 1. Authentication Log File

Created `auth.log` containing sample authentication events.

The log includes:
- Failed password attempts.
- Successful password attempts.
- Administrator login attempts.
- Root login attempts.
- Source IP addresses.

### 2. Python Log Analyser

Created `cloud_log_analyzer.py` to process authentication logs and extract security information.

The program performs the following operations:

| Operation | Description |
|---|---|
| Failed Login Detection | Counts failed password attempts |
| Successful Login Detection | Counts accepted password attempts |
| Admin Detection | Counts log entries containing admin |
| Root Detection | Counts log entries containing root |
| Risk Assessment | Assigns a risk level based on failed attempts |
| Report Generation | Saves results into a text file |

### 3. Risk Level Assessment

The program assigns risk levels based on the number of failed login attempts.

| Failed Login Attempts | Risk Level |
|---|---|
| 0–2 | LOW |
| 3–4 | MEDIUM |
| 5 or more | HIGH |

### 4. Recommended Security Actions

**LOW Risk**
- No immediate action required.

**MEDIUM Risk**
- Monitor login activity.
- Review authentication logs.

**HIGH Risk**
- Investigate possible brute-force attacks.
- Lock suspicious accounts.

### 5. Automated Security Report

The program generates `security_report.txt` containing:

- Failed login attempts.
- Successful logins.
- Admin login attempts.
- Root login attempts.
- Assigned risk level.

## How to Run the Project

### Step 1: Activate Virtual Environment

```
source venv/bin/activate
```

### Step 2: Run the Python Program

```
python3 cloud_log_analyzer.py
```

### Step 3: View the Generated Report

```
cat security_report.txt
```

## Expected Output

```
========== CLOUD SECURITY REPORT ==========

Failed Login Attempts : 3
Successful Logins     : 2
Admin Login Attempts  : 2
Root Login Attempts   : 1
Risk Level            : MEDIUM

========== RECOMMENDED ACTIONS ==========

- Monitor login activity
- Review authentication logs

Security report saved as security_report.txt
```

## Error Handling

Implemented `try-except` using `FileNotFoundError` to handle situations where the authentication log file is missing.

## Screenshots

The `screenshots/` directory contains evidence of the project implementation, Python program execution, authentication log analysis, and generated security report.

## Learning Outcomes

I practised Python-based security log analysis, authentication event detection, login attempt counting, basic risk assessment, conditional logic, file handling, and automated security report generation.

## Project Status

Completed – Day 18 of the Python Cloud Security Learning Roadmap.

**Next:** Day 19 – Advanced Python for Cloud Security.


---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 18

