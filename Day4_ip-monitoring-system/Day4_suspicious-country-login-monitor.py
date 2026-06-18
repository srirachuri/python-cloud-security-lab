# Suspicious Country Login Monitor

A Python-based security monitoring project that detects login attempts from suspicious countries and categorises them based on risk levels.

## Project Overview

This project simulates a basic Security Operations Centre (SOC) monitoring tool.

The script reviews login activity from different countries and classifies each login as:

- Normal Activity
- High Risk Login
- Review Required

This helps demonstrate how security analysts identify potentially suspicious login attempts from specific geographic locations.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Monitors login activity by country
- Detects high-risk countries
- Flags countries requiring manual review
- Uses Python lists, loops, and conditional statements
- Generates a simple security report


## Code Example

```
countries = [
    "India",
    "China",
    "Russia",
    "Canada",
    "Ukraine",
    "Nigeria"
]

for country in countries:
    if country == "China" or country == "Russia":
        print("HIGH RISK LOGIN:", country)

    elif country == "Ukraine" or country == "Nigeria":
        print("Review login activity from:", country)

    else:
        print("Normal activity:", country)
```

## Sample Output

```
--- LOGIN MONITOR REPORT ---

Normal activity: India
HIGH RISK LOGIN: China
HIGH RISK LOGIN: Russia
Normal activity: Canada
Review login activity from: Ukraine
Review login activity from: Nigeria
```

## Learning Objectives

This project helped me practice:

- Python Lists
- For Loops
- If / Elif / Else Conditions
- Security Monitoring Concepts
- Risk Classification
- Linux Terminal Operations

## Cybersecurity Relevance

Security teams often analyse login locations to detect:

- Unauthorised access attempts
- Suspicious geographic logins
- Account compromise indicators
- Potential brute-force attacks
- Unusual user behavior

## Future Improvements

- Read login data from a file
- Store suspicious events in logs
- Generate alerts automatically
- Add risk scores
- Export reports to CSV

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
