# Day 19 – Python JSON Handling for Cloud Security

## Overview

This project demonstrates how to handle JSON (JavaScript Object Notation) files using Python.

JSON is a lightweight data format commonly used for storing and exchanging information in cloud environments.

In cloud security, JSON is commonly used in:
- Cloud APIs (AWS, Azure, GCP)
- IAM policies
- Configuration files
- Security logs
- SIEM tools
- CloudTrail logs
- REST APIs

The project focuses on reading JSON data, writing JSON reports, detecting security risks, and handling file-related exceptions.

## Learning Objectives

- Understand JSON data format.
- Import Python's built-in `json` module.
- Read JSON files using `json.load()`.
- Write JSON files using `json.dump()`.
- Format JSON output using `indent=4`.
- Extract user security information.
- Detect security risks based on failed login attempts.
- Identify administrator accounts.
- Handle missing and invalid JSON files.

## Technologies Used

- Python 3
- JSON
- Linux
- VS Code
- Git and GitHub

## Project Structure

```
Day-19-Python-JSON-Handling-Cloud-Security/
│
├── README.md
├── user_data.json
├── read_json.py
├── write_json.py
├── report.json
├── security_report.py
├── safe_read_json.py
└── screenshots/
```

## Practical Implementation

### 1. Create a JSON File

Created `user_data.json` containing sample user security information.

Example:

```
{
    "username": "admin",
    "failed_logins": 8,
    "country": "India",
    "is_admin": true
}
```

### 2. Read JSON Data

Created `read_json.py` to read JSON data using:

```python
import json

with open("user_data.json", "r") as file:
    data = json.load(file)
```

Extracted and displayed:
- Username
- Failed login attempts
- Country
- Administrator status

### 3. Write JSON Data

Created `write_json.py` to generate JSON reports using `json.dump()`.

The generated `report.json` contains sample user information.

Used `indent=4` to format the JSON output for readability.

### 4. Security Risk Detection

Created `security_report.py` to analyse JSON user information and assign security risk levels based on failed login attempts.

**Risk Assessment:**

| Failed Login Attempts | Risk Level |
|---|---|
| 0–2 | LOW |
| 3–4 | MEDIUM |
| 5–9 | HIGH |
| 10 or more | CRITICAL |

The program also identifies whether the account has administrator privileges.

### 5. Exception Handling

Created `safe_read_json.py` to handle common JSON file errors.

Implemented:
- `FileNotFoundError` – Handles missing JSON files.
- `json.JSONDecodeError` – Handles invalid JSON formatting.

## Expected Security Report

Using the sample JSON data:

```
====== CLOUD SECURITY REPORT ======

Username: admin
Country: India
Failed Logins: 8
Risk Level: HIGH
Administrator Account: YES
```

## How to Run the Project

### Step 1: Activate Virtual Environment

```
source venv/bin/activate
```

### Step 2: Read JSON

```
python3 read_json.py
```

### Step 3: Write JSON

```
python3 write_json.py
```

### Step 4: Run Security Risk Detection

```
python3 security_report.py
```

### Step 5: Test Exception Handling

```
python3 safe_read_json.py
```

### Step 6: View Generated JSON Report

```
cat report.json
```

## Python Concepts Practised

| Function / Concept | Purpose |
|---|---|
| `import json` | Import JSON module |
| `json.load()` | Read JSON from a file |
| `json.dump()` | Write JSON to a file |
| `indent=4` | Format JSON output |
| `if-elif-else` | Security risk classification |
| `try-except` | Exception handling |
| `FileNotFoundError` | Handle missing files |
| `JSONDecodeError` | Handle invalid JSON |

## Learning Outcomes

Successfully practised Python JSON handling, reading and writing structured data, analysing user security information, detecting authentication risks, identifying administrator accounts, and handling JSON-related exceptions.

These concepts provide a foundation for working with cloud APIs, IAM configurations, and security monitoring data.

## Project Status

**Completed – Day 19 of the Python Cloud Security Learning Roadmap.**

Next: Day 20 – Continue Python for Cloud Security.
