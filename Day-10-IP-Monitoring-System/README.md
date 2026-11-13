# Day 10 – IP Monitoring System Using Python

## Project Overview

The IP Monitoring System is a beginner-friendly Python project that simulates basic IP-based security monitoring.

The program maintains a predefined list of blocked IP addresses and uses Python lists and `for` loops to process the addresses and generate a security report.

It displays each blocked IP address with a corresponding security status.

This project demonstrates how Python can be used to organise IP address information and automate simple security reporting tasks.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Project Objectives

- Understand Python lists.
- Practise `for` loops.
- Store multiple IP addresses.
- Iterate through IP address collections.
- Generate blocked IP reports.
- Understand basic IP monitoring concepts.
- Practise security reporting automation.

## Monitoring Logic

The program follows these steps:

1. Creates a list of blocked IP addresses.
2. Displays a blocked IP report heading.
3. Iterates through the IP address list using a `for` loop.
4. Retrieves each IP address.
5. Displays each address with a BLOCKED IP label.

## Example Blocked IP Addresses

- 192.168.1.10
- 10.0.0.9
- 172.16.5.4
- 45.67.23.9

## Project Structure

```
Day-10-IP-Monitoring-System/
│
├── ip_monitor.py
├── README.md
│
└── screenshots/
    ├── ip-monitor-code.png
    └── ip-monitor-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-10-IP-Monitoring-System
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Run the Python program

```
python3 ip_monitor.py
```

## Sample Output

```
--- BLOCKED IP REPORT ---

BLOCKED IP 192.168.1.10
BLOCKED IP 10.0.0.9
BLOCKED IP 172.16.5.4
BLOCKED IP 45.67.23.9
```

## Skills Demonstrated

- Python lists
- Python `for` loops
- Iterating through collections
- IP address identification concepts
- Security report generation
- Basic network security concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python lists and loops can be used to organise IP addresses and generate simple security monitoring reports.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. The program uses manually defined IP addresses and does not monitor live network traffic, inspect packets, enforce firewall rules, or automatically block IP addresses.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 10
