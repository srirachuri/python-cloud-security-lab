# Password Strength Checker

A Python cybersecurity project that evaluates password strength based on password length and classifies it as Weak, Medium, or Strong.

## Project Overview

This project simulates a basic password security validation tool used in cybersecurity and cloud security environments.

The program accepts a password from the user and determines its strength using predefined rules.

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Accepts user password input
- Uses Python functions
- Evaluates password strength
- Classifies passwords as:
  - Weak Password
  - Medium Password
  - Strong Password
- Demonstrates conditional statements and return values

## Code Example

```
def check_password_strength(password):
    if len(password) >= 12:
        return "STRONG PASSWORD"
    elif len(password) >= 8:
        return "MEDIUM PASSWORD"
    else:
        return "WEAK PASSWORD"

password = input("Enter Password: ")

result = check_password_strength(password)

print(result)
```

## Sample Output

### Weak Password

```
Enter Password: Sri
WEAK PASSWORD
```

### Medium Password

```
Enter Password: Rachuri1
MEDIUM PASSWORD
```

### Strong Password

```
Enter Password: SriGayathri123
STRONG PASSWORD
```

## Learning Objectives

This project helped me practice:

- Python Functions
- Function Parameters
- Return Statements
- If / Elif / Else Conditions
- User Input Handling
- Password Security Concepts

## Cybersecurity Relevance

Strong passwords are essential for protecting:

- User Accounts
- Cloud Resources
- Administrative Access
- Sensitive Data
- Enterprise Systems

Security teams often enforce password policies to reduce the risk of:

- Brute-force attacks
- Credential stuffing
- Unauthorized access
- Account compromise


## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
