# Day 2 – Brute Force Detector

## Project Overview

This Python project simulates a simple brute-force attack detection system. It monitors the number of failed login attempts and classifies the activity into different security levels.

This project demonstrates how conditional statements can be used to identify suspicious login behaviour in cybersecurity monitoring.

---

## Features

- Accepts username input
- Accepts failed login attempts
- Detects suspicious login activity
- Displays three security levels:
  - SAFE
  - WARNING
  - CRITICAL ALERT

---

## Technologies Used

- Python 3
- Ubuntu
- Oracle VirtualBox

---

## Program Logic

| Failed Login Attempts | Status |
|-----------------------|--------|
| Less than 5 | SAFE |
| 5 to 9 | WARNING |
| 10 or more | CRITICAL ALERT |

---

## Sample Output

### SAFE

```
Enter the username: Sri Gayathri
Enter the failed login attempts: 3

SAFE: Normal activity for Sri Gayathri
```

### WARNING

```
Enter the username: Sri Gayathri
Enter the failed login attempts: 9

WARNING: Suspicious login activity for Sri Gayathri
```

### CRITICAL ALERT

```
Enter the username: Admin
Enter the failed login attempts: 12

CRITICAL ALERT! Possible brute force attack detected on Admin
```

---

## Learning Outcomes

- User input using `input()`
- Integer conversion using `int()`
- Conditional statements (`if`, `elif`, `else`)
- Comparing numerical values
- Building a simple cybersecurity detection system
- Running Python programs in Ubuntu Terminal

---

## Future Improvements

- Log suspicious login attempts to a file
- Add date and time stamps
- Count repeated alerts
- Send email notifications
- Read login data from log files

---

## Author

**Sri Gayathri**
