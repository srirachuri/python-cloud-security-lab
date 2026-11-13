# Day 13 – Login Risk Checker Using Python

## Overview

The Login Risk Checker is a beginner-friendly Python security project designed to simulate basic authentication risk classification.

The program accepts the number of failed login attempts and evaluates the login activity using a reusable Python function.

It returns one of three security classifications:

- SAFE
- WARNING
- CRITICAL ALERT

This project demonstrates how Python functions, parameters, conditional statements, and return values can be used to implement basic security analysis logic.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python functions.
- Practise function parameters and arguments.
- Learn how to use `return` statements.
- Analyse failed login attempts.
- Classify authentication risk levels.
- Develop reusable security monitoring logic.
- Practise basic Python security automation.

## Security Classification Logic

| Failed Login Attempts | Risk Classification |
|---|---|
| 0–4 | SAFE |
| 5–9 | WARNING |
| 10 or more | CRITICAL ALERT |

## Project Structure

```
Day-13-Login-Risk-Checker/
│
├── login_checker.py
├── README.md
│
└── screenshots/
    ├── login-risk-checker-code.png
    └── login-risk-checker-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-13-Login-Risk-Checker
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Execute the Python program

```
python3 login_checker.py
```

## Sample Output

### Test 1 – Critical Alert

```
Enter the failed login attempts: 12
CRITICAL ALERT
```

### Test 2 – Warning

```
Enter the failed login attempts: 9
WARNING
```

### Test 3 – Safe

```
Enter the failed login attempts: 3
SAFE
```

## Skills Demonstrated

- Python functions
- Function parameters and arguments
- Return statements
- Conditional statements (`if`, `elif`, `else`)
- User input handling
- Authentication risk classification
- Reusable programming logic
- Basic security automation concepts
- Linux command-line operations

## Learning Outcome

Through this project, I learned how Python functions can return security classifications based on failed login attempts.

I practised writing reusable functions and separating security analysis logic from user input and output.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Disclaimer

This is an educational simulation. The program uses manually entered failed login counts and does not monitor actual authentication systems, detect real attacks, or automatically block accounts.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 13
