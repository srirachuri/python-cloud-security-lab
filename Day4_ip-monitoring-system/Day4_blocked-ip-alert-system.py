# Blocked IP Alert System

A Python-based cybersecurity project that generates security alerts when traffic is detected from blocked IP addresses.

## Project Overview

This project simulates a simple Security Operations Centre (SOC) alerting system.

The script monitors a list of blocked IP addresses and generates alerts whenever activity is detected from those IPs.

This type of monitoring is commonly used in cybersecurity environments to identify malicious traffic and investigate potential threats.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Maintains a list of blocked IP addresses
- Generates security alerts for suspicious traffic
- Uses Python lists and loops
- Produces a simple security report
- Demonstrates basic security automation concepts

## Project Structure

```
blocked_ip_alert.py
```

## Code Example

```
blocked_ips = [
    "192.168.1.100",
    "10.0.0.5",
    "45.67.34.9",
    "203.0.113.45"
]

print("--- SECURITY ALERT REPORT ---")

for ip in blocked_ips:
    print("ALERT: Traffic Detected from Blocked IP:", ip)
```

## Sample Output

```
--- SECURITY ALERT REPORT ---

ALERT: Traffic Detected from Blocked IP: 192.168.1.100
ALERT: Traffic Detected from Blocked IP: 10.0.0.5
ALERT: Traffic Detected from Blocked IP: 45.67.34.9
ALERT: Traffic Detected from Blocked IP: 203.0.113.45
```

## Learning Objectives

This project helped me practice:

- Python Lists
- For Loops
- Security Alert Generation
- Basic Security Monitoring
- Linux Terminal Operations
- Python Script Execution

## Cybersecurity Relevance

Security teams use alerting systems to:

- Detect malicious network activity
- Monitor blocked IP addresses
- Investigate potential attacks
- Improve incident response
- Strengthen network security

## Future Improvements

- Read IPs from a log file
- Export alerts to CSV
- Generate alert severity levels
- Send email notifications
- Store alerts in a database

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
