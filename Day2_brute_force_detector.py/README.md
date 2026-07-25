# Day 2: Brute Force Detector

## 📌 Objective
Build an enhanced Python-based Brute Force Detector that classifies login attempts into different security levels based on the number of failed login attempts.

This project introduces multiple conditional statements to simulate a simple authentication monitoring system used in cybersecurity environments.

---

## 🛠 Technologies Used

- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- Nano Text Editor
- Linux Terminal
- Python Virtual Environment (venv)

---

## 📚 Concepts Learned

- Variables
- User Input (`input()`)
- Integer Conversion (`int()`)
- Conditional Statements (`if`, `elif`, `else`)
- Comparison Operators
- Multiple Decision Making
- Python Virtual Environment
- Basic Security Monitoring

---

## ⚡ Code Used

### Activate Virtual Environment

```
source venv/bin/activate
```

### Create/Edit Python Script

```
nano login_alert.py
```

### Run the Program

```
python3 login_alert.py
```

### Program Logic

```
username = input("Enter the username: ")
failed_logins = int(input("Enter the failed login attempts: "))

if failed_logins >= 10:
    print("CRITICAL ALERT! Possible brute force attack detected on", username)

elif failed_logins >= 5:
    print("WARNING: Suspicious login activity for", username)

else:
    print("SAFE: Normal activity for", username)
```

### Security Levels

| Failed Attempts | Status |
|----------------:|--------|
| 0 – 4 | ✅ Safe |
| 5 – 9 | ⚠️ Warning |
| 10+ | 🚨 Critical Alert |

---

## 🧪 What I Practised

- Activated a Python virtual environment.
- Edited Python scripts using Nano.
- Used multiple conditional statements.
- Classified login attempts into different security levels.
- Executed Python programs from the Linux terminal.
- Simulated basic brute-force attack detection logic.

---

## 📸 Screenshots

### 1. Python Brute Force Detector Script

The screenshot demonstrates:

- Writing the Python program using Nano Editor.
- Implementing multiple security conditions.
- Using `if`, `elif`, and `else` statements.

### 2. Running the Program

The screenshot shows:

- Activating the Python virtual environment.
- Running the Python script.
- Entering a username.
- Testing failed login attempts.
- Displaying the appropriate security warning.

---

## 🔒 Security Notes

- Simulates authentication monitoring.
- Detects suspicious login behaviour.
- Identifies potential brute-force attacks.
- Demonstrates basic security automation using Python.
- Introduces security alert classifications used in real-world monitoring systems.

---

## 🎯 Skills Practised

- Python Programming
- Linux Command Line
- Virtual Environments
- Conditional Logic
- Security Automation Basics
- Authentication Monitoring
- Problem Solving

---

## ✅ Outcome

Successfully developed a Brute Force Detector that:

- Accepts user input.
- Evaluates failed login attempts.
- Classifies login activity into Safe, Warning, or Critical levels.
- Demonstrates how Python can automate basic cybersecurity tasks.

This project strengthens Python programming skills while introducing practical security concepts applicable to Cloud Engineering, Cloud Support, DevOps, and Cloud Security careers.

**Sri Gayathri**
