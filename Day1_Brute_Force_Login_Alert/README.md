# 🛡️ Day 1 – Brute Force Login Alert

## 📌 Project Overview

This Python script detects suspicious login activity based on the number of failed login attempts.

It classifies login attempts into three security levels:

- ✅ Safe Login
- ⚠️ Suspicious Login Activity
- 🚨 Critical Brute Force Attack

This is a beginner-friendly cybersecurity project that demonstrates the use of:

- User input
- Variables
- Conditional statements (`if`, `elif`, `else`)
- Basic security logic

---

## 📂 File Name

```
login_alert.py
```

---

## 💻 Source Code

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

---

## ▶️ How to Run

1. Open Terminal.
2. Navigate to the project folder.
3. Activate the virtual environment (optional).

```
source venv/bin/activate
```

4. Run the program.

```
python3 login_alert.py
```

---

## 🧪 Sample Output

### Example 1

```
Enter the username: Sri Gayathri
Enter the failed login attempts: 9

WARNING: Suspicious login activity for Sri Gayathri
```

### Example 2

```
Enter the username: Admin
Enter the failed login attempts: 12

CRITICAL ALERT! Possible brute force attack detected on Admin
```

### Example 3

```
Enter the username: User1
Enter the failed login attempts: 2

SAFE: Normal activity for User1
```

---

## 📚 Concepts Practiced

- Python Variables
- User Input
- Integer Conversion
- Conditional Statements
- Basic Cybersecurity Logic

---

## 🛡️ Security Use Case

Brute force attacks involve repeatedly attempting passwords until the correct one is found.

Security systems monitor failed login attempts and trigger alerts when thresholds are exceeded.

This project simulates that behaviour using simple Python logic.

---

## 📸 Screenshots

### Source Code

> `Screenshoot_Day_1_Brute_Force_Detector_2.png`

### Program Output

> `Screenshoot_Day_1_Brute_Force_Detector_1.png`

---

## 🚀 Future Improvements

- Store login attempts in a log file
- Add timestamps
- Support multiple users
- Read login data from a CSV file
- Send email alerts
- Generate security reports

---

## 🏷️ Tags

`Python` `Cybersecurity` `Security Automation` `Brute Force Detection`
`Beginner Project` `Cloud Security` `Python Basics`
