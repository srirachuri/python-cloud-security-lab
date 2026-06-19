# Login Risk Checker

A Python cybersecurity project that analyses failed login attempts and classifies the security risk level as Safe, Warning, or Critical Alert.

## Project Overview

This project simulates a basic login monitoring system used by security teams to identify suspicious authentication activity.

The program accepts the number of failed login attempts and determines the risk level based on predefined thresholds.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Accepts user input for failed login attempts
- Uses Python functions
- Classifies login activity into risk levels
- Generates security alerts
- Demonstrates conditional logic and return statements

## Project Structure

```
login_checker.py
```

## Code Example

```python
def check_login_risk(failed_logins):
    if failed_logins >= 10:
        return "CRITICAL ALERT"

    elif failed_logins >= 5:
        return "WARNING"

    else:
        return "SAFE"

failed_logins = int(input("Enter the failed login attempts: "))

result = check_login_risk(failed_logins)

print(result)
```

## Sample Output

### Critical Alert

```
Enter the failed login attempts: 12
CRITICAL ALERT
```

### Warning

```
Enter the failed login attempts: 9
WARNING
```

### Safe

```
Enter the failed login attempts: 3
SAFE
```

## Learning Objectives

This project helped me practice:

- Python Functions
- Function Parameters
- Return Statements
- User Input Handling
- If / Elif / Else Conditions
- Security Risk Classification

## Cybersecurity Relevance

Security teams monitor failed login attempts to:

- Detect brute-force attacks
- Identify unauthorised access attempts
- Monitor account security
- Trigger incident response actions
- Protect cloud and enterprise environments

## Risk Levels

| Failed Login Attempts | Risk Level |
|----------------------|------------|
| 0 – 4 | SAFE |
| 5 – 9 | WARNING |
| 10+ | CRITICAL ALERT |

## Future Improvements

- Track usernames
- Track source IP addresses
- Add account lockout simulation
- Store events in log files
- Generate email alerts
- Calculate dynamic risk scores

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
