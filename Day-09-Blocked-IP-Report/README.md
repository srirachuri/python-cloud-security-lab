# Day 9 – Blocked IP Report Using Python While Loop

## Overview

The Blocked IP Report is a beginner-friendly Python project designed to simulate basic network security alert reporting.

The program maintains a predefined list of blocked IP addresses and uses a Python `while` loop to iterate through the list.

It generates security alerts for each blocked IP address and displays a simple security report.

This project demonstrates how Python lists, index variables, and while loops can be used in basic security automation.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python `while` loops.
- Work with Python lists.
- Learn index-based list access.
- Iterate through IP address collections.
- Generate security alert reports.
- Practise basic network security monitoring concepts.

## Logic

The program follows these steps:

1. Creates a list of blocked IP addresses.
2. Initialises an index variable to zero.
3. Uses a `while` loop to check whether the index is less than the list length.
4. Retrieves the IP address using its index.
5. Prints a security alert.
6. Increments the index until all IP addresses are processed.

## Structure

```
Day-09-Blocked-IP-Report/
│
├── blocked_ip_report.py
├── README.md
│
└── screenshots/
    ├── blocked-ip-report-code.png
    └── blocked-ip-report-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-09-Blocked-IP-Report
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Run the Python program

```
python3 blocked_ip_report.py
```

## Sample Output

```
--- SECURITY REPORT ---

ALERT: Traffic Detected from Blocked IP: 192.168.1.100
ALERT: Traffic Detected from Blocked IP: 10.0.0.5
ALERT: Traffic Detected from Blocked IP: 45.67.34.9
ALERT: Traffic Detected from Blocked IP: 203.0.113.45
```

## Skills Demonstrated

- Python lists
- Python `while` loops
- Index-based list traversal
- List length using `len()`
- Index increment operations
- Security alert generation
- Basic network security concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python `while` loops can process collections of IP addresses using index-based access.

I also practised generating automated security reports using Python.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. The program uses manually defined IP addresses and does not monitor live network traffic, inspect network packets, enforce firewall rules, or automatically block IP addresses.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 9
