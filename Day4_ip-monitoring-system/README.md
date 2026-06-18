# IP Monitoring System

## Overview

IP Monitoring System is a beginner-friendly Python cybersecurity project that monitors blocked IP addresses and generates a security report.

The project simulates a basic Security Operations Centre (SOC) workflow where suspicious or malicious IP addresses are tracked and reported.

## Features

* Store blocked IP addresses
* Display blocked IP reports
* Loop through multiple IP addresses automatically
* Simulate basic security monitoring
* Generate security-focused output

## Technologies Used

* Python 3
* Ubuntu Linux
* VirtualBox
* Nano Text Editor

## Project Structure

```
ip_monitor.py
```

## Code Example

```
blocked_ips = [
    "192.168.1.10",
    "10.0.0.9",
    "172.16.5.4",
    "45.67.23.9"
]

print("--- BLOCKED IP REPORT ---")

for ip in blocked_ips:
    print("BLOCKED IP", ip)
```

## Sample Output

```
--- BLOCKED IP REPORT ---
BLOCKED IP 192.168.1.10
BLOCKED IP 10.0.0.9
BLOCKED IP 172.16.5.4
BLOCKED IP 45.67.23.9
```

## Screenshot

### Program Execution

Upload your screenshot as `screenshot.png` and use:

```
![IP Monitoring System](screenshot.png)
```

## Skills Demonstrated

* Python Lists
* For Loops
* Variables
* Security Monitoring
* IP Address Analysis
* Report Generation
* Linux Command Line

## Cybersecurity Relevance

This project demonstrates concepts commonly used in:

* Security Operations Centres (SOC)
* Network Security Monitoring
* Threat Detection
* Incident Response
* Security Reporting
* IP Blacklisting

Organisations often monitor blocked IP addresses to detect suspicious activity and prevent unauthorised access attempts.

## Learning Outcomes

Through this project, I practised:

* Python programming fundamentals
* Working with lists
* Iteration using loops
* Security monitoring concepts
* Basic threat detection workflows
* Linux-based development

## Author
Sri Gayathri
Aspiring Cloud Security Engineer
