# Day 1: Login Alert System

## 📌 Objective
Learn the fundamentals of Python by building a simple Login Alert System that detects potential brute-force login attempts based on the number of failed login attempts.

---

## 🛠 Technologies Used
- Python 3
- Ubuntu Linux
- Oracle VirtualBox
- Nano Text Editor
- Linux Terminal

---

## 📚 Concepts Learned
- Variables
- User Input (`input()`)
- Integer Conversion (`int()`)
- Conditional Statements (`if` and `else`)
- Comparison Operators
- Python Script Execution
- Basic Security Logic

---

## ⚡ Code Used

### Create the Python Script
```
nano login_alert.py
```

### Run the Program
```
python3 login_alert.py
```

### Program Logic

```
username = input("Enter Username ")
failed_logins = int(input("Enter failed login attempts: "))

if failed_logins >= 5:
    print("ALERT! Possible Brute Force Attack detected on", username)
else:
    print("SAFE: Normal activity for", username)
```

**Explanation:**
- Accepts a username.
- Accepts the number of failed login attempts.
- If failed login attempts are **5 or greater**, an alert is displayed.
- Otherwise, the login activity is considered normal.

---

## 🧪 What I Practised
- Installed and verified Python on Ubuntu.
- Verified Python and pip versions.
- Created a Python script using Nano Editor.
- Accepted user input from the terminal.
- Converted string input into an integer.
- Used conditional statements to make security decisions.
- Executed Python scripts from the Linux terminal.

---

## 📸 Screenshots

### 1. Python Login Alert Script

The screenshot demonstrates:

- Creating the Python program using Nano Editor.
- Writing the login alert logic.
- Using variables and conditional statements.

### 2. Running the Program

The screenshot shows:

- Verifying Python installation.
- Checking pip version.
- Running the Python script.
- Entering a username and failed login attempts.
- Displaying the security status based on user input.

---

## 🔒 Security Notes
- Simulates a basic authentication monitoring system.
- Demonstrates how failed login attempts can trigger security alerts.
- Introduces brute-force attack detection concepts.
- Uses simple conditional logic for security decision-making.
- Builds a foundation for future Cloud Security automation projects.

---

## 🎯 Skills Practiced
- Python Programming
- Linux Command Line
- User Input Handling
- Conditional Statements
- Security Automation Basics
- Problem Solving
- Python Script Execution

---

## ✅ Outcome

Successfully built a basic Login Alert System that:

- Accepts user credentials.
- Detects suspicious failed login attempts.
- Generates security alerts based on predefined conditions.
- Strengthened Python fundamentals and introduced beginner-level security automation concepts.

This project serves as the first step toward building Python skills for Cloud Engineering, Cloud Support, DevOps, and Cloud Security careers.
