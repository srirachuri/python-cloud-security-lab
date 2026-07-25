# Day 3 – Security Tracker

## Project Overview

This Python project simulates a basic security monitoring system. It collects login information, generates a security report, displays a list of IP addresses, and detects suspicious login activity based on the number of failed login attempts.

This project introduces simple security reporting and demonstrates how Python can be used for basic cybersecurity monitoring.

---

## Features

- Accepts username input
- Accepts failed login attempts
- Displays a security report
- Shows admin access status
- Displays monitored IP addresses
- Detects suspicious login activity

---

## Technologies Used

- Python 3
- Ubuntu
- Oracle VirtualBox

---

## Program Logic

1. Enter the username.
2. Enter the number of failed login attempts.
3. Display a security report.
4. Display monitored IP addresses.
5. If failed login attempts are **5 or more**, display a warning.
6. Otherwise, display that the activity is normal.

---

## Sample Output

```
Enter username: Sri Gayathri
Enter Failed Logins: 8

---SECURITY REPORT---

Username: Sri Gayathri
Failed Logins: 8
Admin Access: True

192.168.1.10
10.0.0.8
172.16.5.4
192.168.100.25

WARNING: Suspicious Activity Detected!
```

---

## Learning Outcomes

- User input with `input()`
- Integer conversion using `int()`
- Variables and formatted output
- Conditional statements (`if` / `else`)
- Working with lists
- Printing structured security reports
- Building a simple cybersecurity monitoring script

---

## Future Improvements

- Validate IP addresses automatically
- Read IPs from a log file
- Save reports to a text file
- Add timestamps to each report
- Detect repeated login attempts from the same IP
- Export reports in CSV format

---

## Author

**Sri Gayathri**
