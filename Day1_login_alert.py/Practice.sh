# Brute Force Detector 

## Overview

This project is a simple Python-based brute-force detection tool.

The script monitors failed login attempts and classifies activity into three security levels:

- SAFE
- WARNING
- CRITICAL ALERT

This simulates how cloud security and SOC teams detect suspicious authentication activity.

---

## Features

✅ User login monitoring

✅ Failed login attempt tracking

✅ Suspicious activity detection

✅ Brute-force attack alerting

✅ Multiple security severity levels

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Nano Editor

---

## Source Code

```python
username = input("Enter the username: ")
failed_logins = int(input("Enter the failed login attempts: "))

if failed_logins >= 10:
    print("CRUTIAL ALERT! Possible brute force attack detected on", username)

elif failed_logins >= 5:
    print("WARNING: Suspicious login activity for", username)

else:
    print("SAFE: Normal activity for", username)
```

---

## How to Run

```bash
python3 login_alert.py
```

---

## Example Outputs

### Safe Activity

```text
Enter the username: Sri Gayathri
Enter the failed login attempts: 2

SAFE: Normal activity for Sri Gayathri
```

### Warning Activity

```text
Enter the username: Sri Gayathri
Enter the failed login attempts: 7

WARNING: Suspicious login activity for Sri Gayathri
```

### Critical Alert

```text
Enter the username: admin
Enter the failed login attempts: 15

CRITICAL ALERT! Possible brute force attack detected on admin
```

---

## Security Logic

| Failed Attempts | Status |
|----------------|---------|
| 0 - 4 | SAFE |
| 5 - 9 | WARNING |
| 10+ | CRITICAL ALERT |

---

## Skills Demonstrated

- Python Programming
- Conditional Statements
- User Input Handling
- Security Monitoring
- Authentication Security
- Brute Force Detection Logic

---

## Cybersecurity Relevance

Brute-force attacks are common threats against:

- Linux Servers
- Cloud Accounts
- SSH Services
- Web Applications
- IAM Accounts

Security teams often monitor repeated failed login attempts and trigger alerts when thresholds are exceeded.

---

## Future Improvements

- Add IP Address Tracking
- Log Events to Files
- Email Notifications
- CloudWatch Integration
- SIEM Integration
- Dashboard Reporting

---

## Learning Outcomes

Through this project, I learned:

- Python input handling
- Decision making using if-elif-else
- Security alert generation
- Authentication monitoring concepts
- Basic brute-force attack detection

---

## Author

Sri Gayathri

BCA Student | Linux Learner | Future Cloud Security Engineer

Learning:
- Python
- Linux
- Networking
- AWS
- Cloud Security
