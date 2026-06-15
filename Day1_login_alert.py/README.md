# Day 1 – Login Alert System 

## Overview

The program monitors failed login attempts and generates an alert when suspicious activity is detected. This simulates a basic security monitoring system used by SOC analysts and cloud security teams.

---

## Objective

- Learn Python input handling
- Use conditional statements
- Simulate login monitoring
- Detect potential brute-force attacks
- Build a simple cybersecurity project

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Nano Editor

---


## Python Code

```python
username = input("Enter Username ")
failed_logins = int(input("Enter failed login attempts: "))

if failed_logins >= 5:
    print("ALERT! Possible Brute Force Attack detected on", username)
else:
    print("SAFE: Normal activity for", username)
```

---

## How to Run

Run the script:

```bash
python3 login_alert.py
```

---

## Example Output

### Normal Activity

```text
Enter Username Sri Gayathri
Enter failed login attempts: 4

SAFE: Normal activity for Sri Gayathri
```

### Suspicious Activity

```text
Enter Username admin
Enter failed login attempts: 8

ALERT! Possible Brute Force Attack detected on admin
```

---

## Skills Demonstrated

- Variables
- User Input
- Integer Conversion
- Conditional Statements
- Security Logic
- Python Fundamentals

---

## Security Relevance

This project introduces a basic concept used in:

- SOC Operations
- Cloud Security Monitoring
- Login Auditing
- Brute Force Detection
- Security Automation

Many enterprise systems generate alerts when multiple login failures occur within a short period of time.

---

## Learning Outcomes

Through this program, I learned:

- How to take user input in Python
- How to use if-else conditions
- How login monitoring works
- How brute-force attacks are detected
- How security alerts are generated

---

## Author

Sri Gayathri

BCA Student | Linux Learner | Future Cloud Security Engineer

Learning Focus:
- Python
- Linux
- Networking
- AWS Cloud
- Cloud Security
