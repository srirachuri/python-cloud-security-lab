# Day 1 – Login Alert System

## Project Overview
This Python project simulates a basic login monitoring system. It asks for a username and the number of failed login attempts. If the failed attempts are 5 or more, it displays a security alert indicating a possible brute-force attack. Otherwise, it reports normal activity.

## Features
- Accepts username input
- Accepts failed login attempt count
- Detects possible brute-force attacks
- Displays security status (SAFE or ALERT)

## Technologies Used
- Python 3
- Ubuntu
- Oracle VirtualBox

## Program Logic
- Input username
- Input number of failed login attempts
- If failed attempts are **5 or greater**:
  - Display **ALERT**
- Otherwise:
  - Display **SAFE**

## Sample Output

### Safe Login
```
Enter Username: Sri Gayathri
Enter failed login attempts: 4
SAFE: Normal activity for Sri Gayathri
```

### Suspicious Login
```
Enter Username: Admin
Enter failed login attempts: 7
ALERT! Possible Brute Force Attack detected on Admin
```

## Learning Outcomes
- Using `input()`
- Converting input with `int()`
- Conditional statements (`if` / `else`)
- Basic cybersecurity monitoring logic
- Running Python programs in Ubuntu Terminal

## Author
Sri Gayathri
