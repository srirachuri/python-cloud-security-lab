# Security Monitor System 
## Overview

This project is a simple Python-based Security Monitoring System that analyses login activity and generates security alerts based on:

- Blocked attacker IP addresses
- Failed login attempts
- Foreign login locations

The script simulates how Security Operations Centre (SOC) analysts and Cloud Security Engineers monitor authentication events and detect suspicious behaviour.

---

## Features

✅ User login monitoring

✅ Blocked IP detection

✅ Brute-force attack detection

✅ Foreign login detection

✅ Security report generation

✅ Multiple alert levels

---

## Technologies Used

- Python 3
- Ubuntu Linux
- Nano Editor

---

## Source Code

```
username = input("Enter username: ")
ip_address = input("Enter ip_address: ")
failed_logins = int(input("Enter failed login attempts: "))
country = input("Enter Login Country: ")

blocked_ips = ["192.168.1.100", "10.0.0.5", "45.67.23.9"]

print("\n--- SECURITY REPORT ---")
print("username:", username)
print("ip_address:", ip_address)
print("failed_logins:", failed_logins)
print("country:", country)

if ip_address in blocked_ips:
    print("CRITICAL ALERT: Blocked attacker IP detected!")

if failed_logins >= 5:
    print("WARNING: Possible Brute force attack")
else:
    print("SAFE: Normal login activity")

# Foreign login detection
if country != "India":
    print("ALERT: Foreign Login Detected!")
```

---

## How to Run

```
python3 security_monitor.py
```

---

## Example Output

### Suspicious Login

```
Enter username: Sri Gayathri
Enter ip_address: 10.0.0.5
Enter failed login attempts: 9
Enter Login Country: Venezuela

--- SECURITY REPORT ---
username: Sri Gayathri
ip_address: 10.0.0.5
failed_logins: 9
country: Venezuela

CRITICAL ALERT: Blocked attacker IP detected!
WARNING: Possible Brute force attack
ALERT: Foreign Login Detected!
```
## Example Output
### Suspicious Login
```
Enter username: Sri Gayathri
Enter ip_address: 10.0.0.5
Enter failed login attempts: 9
Enter Login Country: Venezuela

--- SECURITY REPORT ---
username: Sri Gayathri
ip_address: 192.168.1.10
failed_logins: 2
country: India

SAFE: Normal login activity
```

---

## Security Checks Performed

| Check | Alert Trigger |
|---------|---------------|
| Blocked IP Detection | IP found in blacklist |
| Failed Login Detection | 5 or more failed attempts |
| Foreign Login Detection | Country not equal to India |

---

## Skills Demonstrated

- Python Variables
- Data Types
- Lists
- User Input Handling
- Conditional Statements
- Security Monitoring Logic
- Basic Threat Detection

---

## Cybersecurity Relevance

This project demonstrates concepts used in:

- SOC Monitoring
- SIEM Alerting
- Cloud Security Operations
- Identity and Access Management (IAM)
- Threat Detection
- Login Auditing

Security teams commonly investigate:

- Login attempts from blacklisted IP addresses
- Multiple failed authentication attempts
- Access from unexpected countries

---

## Learning Outcomes

Through this project, I learned:

- How to work with variables and data types
- How to store data in Python lists
- How to use conditional logic
- How security alerts are generated
- How authentication events are monitored

---

## Author

Sri Gayathri

BCA Student | Linux Learner | Future Cloud Security Engineer

Learning Focus:
- Python
- Linux
- Networking
- AWS
- Cloud Security
- SOC Operations
