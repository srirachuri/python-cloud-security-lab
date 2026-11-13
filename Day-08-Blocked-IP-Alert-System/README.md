# Day 8 – Blocked IP Alert System

## Overview

The Blocked IP Alert System is a beginner-friendly Python project that simulates basic network security alert monitoring.

The program maintains a predefined list of blocked IP addresses and uses a Python `for` loop to iterate through the list and generate security alerts for each IP address.

This project demonstrates how Python lists and loops can be used to organise and display basic security monitoring information.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Understand Python lists.
- Practise `for` loops.
- Store multiple IP addresses in a list.
- Iterate through IP addresses.
- Generate security alerts.
- Understand basic IP-based security monitoring concepts.

## Security Monitoring Logic

The program uses a predefined list of blocked IP addresses.

When executed, it:

1. Stores blocked IP addresses in a Python list.
2. Displays a security alert report.
3. Iterates through the list using a `for` loop.
4. Prints an alert for each blocked IP address.

## Structure

```
Day-08-Blocked-IP-Alert-System/
│
├── blocked_ip_alert.py
├── README.md
│
└── screenshots/
    ├── blocked-ip-alert-code.png
    └── blocked-ip-alert-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-08-Blocked-IP-Alert-System
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Execute the Python program

```
python3 blocked_ip_alert.py
```

## Sample Output

```
--- SECURITY ALERT REPORT ---

ALERT: Traffic Detected from Blocked IP: 192.168.1.100
ALERT: Traffic Detected from Blocked IP: 10.0.0.5
ALERT: Traffic Detected from Blocked IP: 45.67.34.9
ALERT: Traffic Detected from Blocked IP: 203.0.113.45
```

## Skills Demonstrated

- Python lists
- Python `for` loops
- Iterating through collections
- IP address identification concepts
- Security alert generation
- Basic network security concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python lists and loops can be used to maintain IP address collections and generate security alerts.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. The program uses manually defined IP addresses and does not monitor live network traffic, inspect packets, enforce firewall rules, or automatically block IP addresses.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 8
