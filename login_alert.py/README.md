# Login Alert System (Python)

## Overview
A simple Python script that simulates a login monitoring system by checking the number of failed login attempts. If the failed attempts reach a defined threshold, the program generates a brute-force attack alert.

## Features
- Accepts a username as input.
- Accepts the number of failed login attempts.
- Detects possible brute-force attacks.
- Displays a security alert when failed login attempts are 5 or more.
- Displays a normal activity message otherwise.

## Technologies Used
- Python 3
- Linux (Ubuntu)
- Oracle VirtualBox

## How to Run

```
python3 login_alert.py
```

## Example Output

### Safe Login
```
Enter Username: Sri
Enter failed login attempts: 4
SAFE: Normal activity for Sri
```

### Alert
```
Enter Username: Admin
Enter failed login attempts: 6
ALERT! Possible Brute Force Attack detected on Admin
```

## Code Logic

1. Take the username as input.
2. Take the failed login attempts as input.
3. If failed attempts are 5 or greater:
   - Display a brute-force attack alert.
4. Otherwise:
   - Display a normal activity message.

## Learning Outcomes
- User input using `input()`
- Integer conversion with `int()`
- Conditional statements (`if` / `else`)
- Basic cybersecurity alert logic
- Running Python programs on Ubuntu Linux

## Future Improvements
- Monitor multiple users.
- Store login attempts in a log file.
- Add timestamps for each login event.
- Read login data from a file.
- Send email or Slack alerts for suspicious activity.

## Author
Sri Gayathri
