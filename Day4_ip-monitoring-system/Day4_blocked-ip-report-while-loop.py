# Blocked IP Report (While Loop)

A Python cybersecurity project that generates security alerts for blocked IP addresses using a while loop.

## Project Overview

This project simulates a basic security monitoring system that reviews a list of blocked IP addresses and generates alerts when suspicious traffic is detected.

Unlike many beginner projects that use for loops, this project demonstrates how to use a while loop to process security data.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Stores blocked IP addresses in a list
- Uses a while loop for iteration
- Generates security alerts
- Demonstrates index-based list processing
- Produces a simple security report

## Project Structure

```text
blocked_ip_report.py
```

## Code Example

```python
blocked_ips = [
    "192.168.1.100",
    "10.0.0.5",
    "45.67.23.9",
    "203.0.113.45"
]

print("--- SECURITY REPORT ---")

index = 0

while index < len(blocked_ips):
    print(
        "ALERT: Traffic Detected from Blocked IP:",
        blocked_ips[index]
    )
    index += 1
```

## Sample Output

```text
--- SECURITY REPORT ---

ALERT: Traffic Detected from Blocked IP: 192.168.1.100
ALERT: Traffic Detected from Blocked IP: 10.0.0.5
ALERT: Traffic Detected from Blocked IP: 45.67.23.9
ALERT: Traffic Detected from Blocked IP: 203.0.113.45
```

## Learning Objectives

This project helped me learn:

- Python Lists
- While Loops
- Index-Based Iteration
- Security Monitoring Concepts
- Basic Alert Generation
- Linux Terminal Operations

## Cybersecurity Relevance

Security analysts often review lists of suspicious or blocked IP addresses to:

- Detect malicious activity
- Investigate security incidents
- Monitor network traffic
- Improve threat detection

## Future Improvements

- Read IP addresses from a file
- Add risk severity levels
- Save reports to a log file
- Export alerts to CSV
- Send automated notifications

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
