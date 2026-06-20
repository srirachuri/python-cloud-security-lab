# Password Audit System

A Python cybersecurity project that evaluates password strength and generates a password audit report using a modular design.

## Project Overview

This project simulates a simple password auditing tool used by security teams to review account password strength.

The application separates password validation logic into a reusable module and imports it into the main auditing program.

Passwords are classified as:

- WEAK PASSWORD
- MEDIUM PASSWORD
- STRONG PASSWORD

The audit report displays the username and password security status.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Modular Python design
- Custom function imports
- Password strength validation
- User input handling
- Security audit reporting
- Reusable security functions

## Module: password_checker.py

```
def check_password_strength(password):
    if len(password) >= 12:
        return "STRONG PASSWORD"

    elif len(password) >= 8:
        return "MEDIUM PASSWORD"

    else:
        return "WEAK PASSWORD"
```

## Main Program: password_audit.py

```
from password_checker import check_password_strength

username = input("Enter Username: ")
password = input("Enter Password: ")

result = check_password_strength(password)

print("\n--- PASSWORD AUDIT REPORT ---")
print("Username:", username)
print("Password Status:", result)
```

## Sample Output

### Medium Password

```
Enter Username: Sri Gayathri
Enter Password: Rachuri1

--- PASSWORD AUDIT REPORT ---
Username: Sri Gayathri
Password Status: MEDIUM PASSWORD
```

### Strong Password

```
Enter Username: Sri Gayathri
Enter Password: SriGayathri1234

--- PASSWORD AUDIT REPORT ---
Username: Sri Gayathri
Password Status: STRONG PASSWORD
```

## Learning Objectives

This project helped me practice:

- Python Functions
- Modules and Imports
- Return Statements
- User Input Handling
- Security Reporting
- Password Security Concepts

## Cybersecurity Relevance

Password auditing is important because weak passwords increase the risk of:

- Unauthorized access
- Credential stuffing attacks
- Brute-force attacks
- Account compromise

Security teams regularly audit passwords to ensure compliance with organisational security policies.

## Skills Demonstrated

- Python Fundamentals
- Modular Programming
- Security Automation Basics
- Password Validation
- Code Reusability
- Security Reporting

## Future Improvements

- Check uppercase letters
- Check lowercase letters
- Check numbers
- Check special characters
- Generate password recommendations
- Export audit reports to CSV

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
