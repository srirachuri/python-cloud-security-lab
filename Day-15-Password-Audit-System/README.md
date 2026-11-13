# Day 15 – Password Audit System Using Python

## Overview

The Password Audit System is a beginner-friendly Python project designed to evaluate password strength and generate a basic password security report.

The project uses Python functions and modules to classify passwords into three categories:

- Weak Password
- Medium Password
- Strong Password

It evaluates password strength based on password length and generates an audit report containing the username and password status.

## Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- GNU Nano
- Python Virtual Environment (venv)

## Objectives

- Understand Python functions.
- Learn how to create reusable functions.
- Practise importing functions from another Python file.
- Evaluate password length.
- Classify password strength.
- Generate a basic password audit report.
- Understand fundamental password security concepts.

## Project Architecture

The project contains two Python files.

### 1. password_checker.py

Responsible for:

- Defining the `check_password_strength()` function.
- Checking password length.
- Classifying password strength.
- Returning the appropriate result.

### 2. password_audit.py

Responsible for:

- Collecting username input.
- Collecting password input.
- Importing the password-checking function.
- Generating the password audit report.
- Displaying the password strength classification.

## Password Strength Classification

The project uses the following password-length rules:

| Password Length | Classification |
|---|---|
| Below 8 characters | WEAK PASSWORD |
| 8–11 characters | MEDIUM PASSWORD |
| 12 or more characters | STRONG PASSWORD |

**Note:** This is a basic educational password-strength simulation. It evaluates length only and does not check character variety, breached passwords, or password entropy.

## Project Structure

```
Day-6-Password-Audit-System/
│
├── password_checker.py
├── password_audit.py
├── README.md
│
└── screenshots/
    ├── password-checker-code.png
    ├── password-audit-code.png
    └── password-audit-output.png
```

## How to Run

### Step 1: Clone the repository

```
git clone https://github.com/YOUR-USERNAME/cloud-security-projects.git
```

### Step 2: Navigate to the project directory

```
cd cloud-security-projects/Day-6-Password-Audit-System
```

### Step 3: Activate the virtual environment

```
source venv/bin/activate
```

### Step 4: Run the program

```
python3 password_audit.py
```

**Important:** Keep both Python files in the same directory so that `password_audit.py` can import `password_checker.py`.

## Sample Output

### Test 1 – Weak Password

```
--- PASSWORD AUDIT REPORT ---
Username: Demo User
Password Status: WEAK PASSWORD
```

### Test 2 – Medium Password

```
--- PASSWORD AUDIT REPORT ---
Username: Demo User
Password Status: MEDIUM PASSWORD
```

### Test 3 – Strong Password

```
--- PASSWORD AUDIT REPORT ---
Username: Demo User
Password Status: STRONG PASSWORD
```

## Skills Demonstrated

- Python functions
- Function parameters
- Return statements
- Python modules
- Import statements
- Conditional statements
- String handling
- User input handling
- Basic password security concepts
- Linux command-line operations

## Learning Outcomes

Through this project, I learned how to create reusable Python functions, organise code into separate modules, import functions, and implement basic password-strength classification.

This project is part of my hands-on Python learning journey focused on Cloud Support and Cloud Security.

## Security Disclaimer

This is an educational simulation. It does not connect to real authentication systems or perform comprehensive password security assessments.

For real applications, passwords should never be stored or displayed in plaintext. Secure password handling, hashing, and additional password-strength checks should be implemented.

---

**Author:** Sri Gayathri Rachuri

**Project:** Python for Cloud Security – Day 15
