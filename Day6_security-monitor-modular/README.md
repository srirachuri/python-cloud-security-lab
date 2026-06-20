# Security Monitor (Modular Python Project)

A Python cybersecurity project that analyses failed login attempts using a modular design with custom Python modules and imports.

## Project Overview

This project simulates a basic Security Operations Centre (SOC) monitoring tool.

The application separates security logic into reusable modules, making the code easier to maintain and scale.

The project evaluates failed login attempts and classifies activity as:

- SAFE
- WARNING
- CRITICAL ALERT

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Modular Python design
- Custom module creation
- Function imports
- User input handling
- Security risk classification
- Reusable security utilities
```

## Module: utils.py

```
def check_login_risk(failed_logins):

    if failed_logins >= 10:
        return "CRITICAL ALERT"

    elif failed_logins >= 5:
        return "WARNING"

    else:
        return "SAFE"
```

## Main Program: security_monitors.py

```
from utils import check_login_risk

failed_logins = int(input("Enter Failed Login Attempts: "))

result = check_login_risk(failed_logins)

print(result)
```

## Sample Output

### Critical Alert

```
Enter Failed Login Attempts: 12
CRITICAL ALERT
```

### Warning

```
Enter Failed Login Attempts: 5
WARNING
```

### Safe

```
Enter Failed Login Attempts: 3
SAFE
```

## Learning Objectives

This project helped me practice:

- Python Functions
- Python Modules
- Import Statements
- Code Reusability
- User Input Handling
- Security Monitoring Concepts

## Cybersecurity Relevance

Security teams often build reusable modules for:

- Login monitoring
- Threat detection
- Alert generation
- Log analysis
- Security automation

Using modular code makes security tools easier to maintain and expand as environments grow.

## Skills Demonstrated

- Python Fundamentals
- Functions
- Modules and Imports
- Security Automation Basics
- Code Organisation
- Cybersecurity Monitoring

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
