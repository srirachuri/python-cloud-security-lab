# Day 17 – Python File I/O for Cloud Security

## Overview

This project demonstrates Python File Input/Output (File I/O) concepts through practical cloud security log analysis exercises.

The main objective is to learn how to read authentication log files, identify failed login attempts, generate security reports, and handle missing files safely.

## Learning Objectives

- Understand Python file handling.
- Use `open()` to access files.
- Read files using `read()`, `readline()`, and `readlines()`.
- Write data using `write()`.
- Use `with open()` for safe file handling.
- Read authentication log files.
- Count failed login attempts.
- Generate automated security reports.
- Handle missing files using `try-except`.

## Technologies Used

- Python 3
- Linux / Windows Terminal
- VS Code
- Git and GitHub

## Project Structure

```
Day-17-Python-File-IO-Cloud-Security/
│
├── README.md
├── auth.log
├── cloud_log_reader.py
├── report_writer.py
├── failed_login_counter.py
├── security_report_generator.py
├── safe_log_reader.py
└── screenshots/
```

## Practical Exercises

### 1. Create an Authentication Log File

Created `auth.log` containing sample authentication events.

Example:

```
Jul 12 09:10 Failed password for admin from 192.168.1.10
Jul 12 09:12 Accepted password for sri from 10.0.0.5
Jul 12 09:15 Failed password for root from 45.67.23.9
```

### 2. Read Log Files

Created `cloud_log_reader.py` to practice:

- Reading the entire file using `read()`.
- Reading individual lines using `readline()`.
- Reading all lines using `readlines()`.
- Iterating through log files using a `for` loop.

### 3. Write to a File

Created `report_writer.py` to write security scan information into `report.txt`.

### 4. Count Failed Login Attempts

Created `failed_login_counter.py` to identify and count failed password attempts in the authentication log.

**Expected output:**

```
Failed Login Attempts: 2
```

### 5. Generate a Security Report

Created `security_report_generator.py` to automatically generate a security report containing failed login statistics.

Example:

```
Security Report
-----------------
Failed Login Attempts: 2
```

### 6. Basic Error Handling

Created `safe_log_reader.py` using `try-except` to handle missing authentication log files.

The program catches `FileNotFoundError` and displays an appropriate error message.

## Key Python Concepts Practised

| Concept | Purpose |
|---|---|
| `open()` | Open files |
| `read()` | Read entire files |
| `readline()` | Read one line |
| `readlines()` | Read all lines into a list |
| `write()` | Write information |
| `with open()` | Safely manage files |
| `for` loop | Process log entries |
| `if` condition | Identify failed logins |
| `try-except` | Handle file errors |

## How to Run

Run the following commands from the project directory:

```
python3 cloud_log_reader.py
python3 failed_login_counter.py
python3 report_writer.py
python3 security_report_generator.py
python3 safe_log_reader.py
```

View the generated report:

```
cat report.txt
```

## Screenshots

The `screenshots/` folder contains evidence of the Python File I/O exercises, program execution, failed login counting, security report generation, and error handling.

## Outcome

I completed Day 17 of the Python Cloud Security learning roadmap.

I practised reading authentication logs, processing security events, counting failed login attempts, generating security reports, and handling file-related errors.

**Next Step:** Continue to Day 18 of the Python Cloud Security learning roadmap.


---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 17

