# Login Risk Analyser

A Python cybersecurity project that analyses login activity and determines security risk levels based on failed login attempts and account privileges.

## Project Overview

This project simulates a Security Operations Centre (SOC) login monitoring system.

The program evaluates:

- Username
- Failed Login Attempts
- Admin Account Status

Based on these inputs, it generates a security report and recommends appropriate actions.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Accepts user login information
- Monitors failed login attempts
- Identifies high-risk admin account activity
- Classifies incidents by severity
- Generates security response recommendations
- Demonstrates real-world security monitoring logic

## Project Structure

```
login_monitor.py
```

## Code Highlights

```
def analyse_login(username, failed_logins, is_admin):

    if failed_logins >= 15:
        print("Risk Level: ACCOUNT LOCKED")

    elif failed_logins >= 10 and is_admin == "Yes":
        print("Risk Level: HIGH PRIORITY SECURITY INCIDENT")

    elif failed_logins >= 10:
        print("Risk Level: CRITICAL INCIDENT")

    elif failed_logins >= 5:
        print("Risk Level: WARNING")

    else:
        print("Risk Level: SAFE")
```

## Sample Output

### Account Locked

```
Enter Username: sri gayathri
Enter Failed Login Attempts: 22
Is this an Admin Account? (Yes/No): No

--- SECURITY REPORT ---

Username: sri gayathri
Risk Level: ACCOUNT LOCKED
Action: Disable Account and Investigate Immediately
```

### Warning

```
Enter Username: SRI GAYATHRI
Enter Failed Login Attempts: 9
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---

Username: SRI GAYATHRI
Risk Level: WARNING
Action: Monitor User Activity
```

### Safe

```text
Enter Username: Sri Gayathri
Enter Failed Login Attempts: 3
Is this an Admin Account? (Yes/No): Yes

--- SECURITY REPORT ---

Username: Sri Gayathri
Risk Level: SAFE
Action: No Immediate Threat
```

## Risk Levels

| Failed Attempts | Condition | Risk Level |
|---------------|-----------|------------|
| 15+ | Any User | ACCOUNT LOCKED |
| 10+ | Admin Account | HIGH PRIORITY SECURITY INCIDENT |
| 10+ | Standard User | CRITICAL INCIDENT |
| 5–9 | Any User | WARNING |
| 0–4 | Any User | SAFE |

## Learning Objectives

This project helped me practice:

- Python Functions
- Parameters
- User Input Handling
- Conditional Logic
- Logical Operators (`and`)
- Security Risk Analysis
- Incident Response Concepts

## Cybersecurity Relevance

Security analysts monitor failed login attempts because they may indicate:

- Brute-force attacks
- Credential stuffing
- Unauthorised access attempts
- Compromised accounts
- Privileged account abuse

Admin account activity is especially important because compromised privileged accounts can lead to major security incidents.

## Future Improvements

- Track source IP addresses
- Store incidents in log files
- Export reports to CSV
- Add account lockout timers
- Generate email alerts
- Create a dashboard for monitoring login events

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
