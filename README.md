# Python for Cloud Security – 20 Days of Hands-On Learning

## About This Repository

This repository documents my 20-day practical Python learning journey focused on Cloud Security, Cloud Support, and Security Automation.

The goal is to develop Python programming skills and apply them to real-world cloud security scenarios, including authentication monitoring, security log analysis, IAM auditing, configuration checks, and automated security reporting.

Each day includes practical exercises, Python scripts, sample data, and project screenshots.

## Learning Objectives

- Learn Python fundamentals and programming concepts.
- Work with files, directories, and Linux commands.
- Read and process security logs.
- Handle JSON, CSV, and YAML data.
- Detect suspicious authentication activity.
- Analyse cloud IAM security configurations.
- Identify security risks and generate reports.
- Automate basic security monitoring tasks.
- Practise Python scripting for cloud environments.

## Technologies and Tools

- Python 3
- Linux
- Bash
- JSON
- CSV
- YAML
- Regular Expressions (Regex)
- Git
- GitHub
- VS Code
- Virtual Environments

## 20-Day Learning Roadmap

### Phase 1: Python Fundamentals (Days 1–8)

| Day | Topic | Practical Learning |
|---|---|---|
| 01 | Python Environment Setup | Python installation, pip, virtual environments, requirements.txt and first Python script |
| 02 | Variables and Data Types | Store usernames, IP addresses and security information |
| 03 | Conditional Statements | Detect failed login attempts and generate security alerts |
| 04 | Loops | Iterate through IP addresses and security log entries |
| 05 | Functions | Create reusable security functions, including password strength checking |
| 06 | Python Modules | Import modules and organise reusable code using utils.py |
| 07 | Python Revision | Practise conditions, functions, modules and SAFE/ALERT logic |
| 08 | File Handling Introduction | Read and write authentication log files using Python |

### Phase 2: Cloud Security Data Processing (Days 9–14)

| Day | Topic | Practical Learning |
|---|---|---|
| 09 | JSON Handling | Read JSON data, dictionaries and cloud IAM login risk analysis |
| 10 | CSV Handling | Process IAM user records, password reports and vulnerability exports |
| 11 | YAML Basics | Read YAML configuration files and perform cloud configuration security checks |
| 12 | Regular Expressions (Regex) | Extract IP addresses, usernames and security events from logs |
| 13 | Enterprise Cloud Security Log Parser | Analyse authentication logs, count failed/successful logins, detect MFA events and generate security reports |
| 14 | Weekly Revision Challenge | Rebuild the Cloud Security Login Analyser using JSON, CSV, YAML and Regex |

### Phase 3: Python for Linux and Cloud Security (Days 15–16)

| Day | Topic | Practical Learning |
|---|---|---|
| 15 | Python OS Module | Work with directories, file permissions and environment variables |
| 16 | Python Subprocess Module | Execute Linux security commands such as ss, netstat, df and ps |

### Phase 4: Practical Cloud Security Projects (Days 17–20)

| Day | Project | Practical Implementation |
|---|---|---|
| 17 | Python File I/O – Cloud Security | Read authentication logs, count failed login attempts and generate reports |
| 18 | Cloud Security Log Analyser | Analyse failed, successful, admin and root login attempts and assign risk levels |
| 19 | Python JSON Handling for Cloud Security | Read and write JSON data, detect security risks and handle JSON exceptions |
| 20 | Cloud IAM Login Risk Analyser | Detect suspicious cloud logins, disabled MFA, foreign login activity and high-risk administrator accounts |

## Detailed Project Highlights

### Day 17 – Python File I/O (Cloud Security Version)

**Files:**
- cloud_log_reader.py
- report_writer.py
- failed_login_counter.py
- security_report_generator.py
- safe_log_reader.py

**Skills Practised:**
- open()
- read()
- readline()
- readlines()
- write()
- with open()
- FileNotFoundError

**Outcome:** Developed Python scripts to read authentication logs, count failed login attempts and generate security reports.

### Day 18 – Cloud Security Log Analyser

**Files:**
- auth.log
- cloud_log_analyzer.py
- security_report.txt

**Features:**
- Count failed login attempts.
- Count successful logins.
- Detect admin login attempts.
- Detect root login attempts.
- Assign LOW, MEDIUM and HIGH risk levels.
- Generate security reports.
- Recommend security actions.

**Outcome:** Developed a basic authentication log analyser using Python.

### Day 19 – Python JSON Handling for Cloud Security

**Files:**
- user_data.json
- read_json.py
- write_json.py
- report.json
- security_report.py
- safe_read_json.py

**Features:**
- Read JSON data.
- Write JSON reports.
- Analyse user security information.
- Detect failed login risks.
- Identify administrator accounts.
- Handle missing and invalid JSON files.

**Outcome:** Practised structured data processing and JSON-based security risk detection.

### Day 20 – Cloud IAM Login Risk Analyser

**Files:**
- iam_login.json
- iam_login_analyzer.py

**Features:**
- Analyse cloud login information.
- Identify suspicious login activity.
- Detect excessive failed login attempts.
- Identify administrator accounts.
- Check MFA status.
- Detect foreign login activity.
- Identify administrator accounts without MFA.
- Assign SAFE, WARNING and CRITICAL risk levels.
- Recommend security response actions.

**Outcome:** Developed a Python-based Cloud IAM Login Risk Analyser using sample AWS login information.

## Key Python Concepts Learned

| Python Concept | Application |
|---|---|
| Variables and Data Types | Store security information |
| Conditions | Identify suspicious events |
| Loops | Process log entries |
| Functions | Build reusable security scripts |
| Modules | Organise Python programs |
| File I/O | Read and write security logs |
| JSON | Process structured cloud data |
| CSV | Process security records |
| YAML | Read configuration files |
| Regex | Extract security information |
| OS Module | Work with Linux directories and permissions |
| Subprocess | Execute Linux commands |
| Exception Handling | Handle file and data errors |

## How to Run Python Projects

### 1. Clone the Repository

```
git clone https://github.com/srirachuri/cloud-security-projects.git
```

### 2. Navigate to a Project Folder

```
cd cloud-security-projects
```

Navigate into the relevant daily project directory.

### 3. Activate Virtual Environment

```
source venv/bin/activate
```

### 4. Run a Python Script

```
python3 filename.py
```

Replace filename.py with the relevant Python script.

## Repository Structure

```
cloud-security-projects/
│
├── Python/
│   ├── Day-01/
│   ├── Day-02/
│   ├── Day-03/
│   ├── Day-04/
│   ├── Day-05/
│   ├── Day-06/
│   ├── Day-07/
│   ├── Day-08/
│   ├── Day-09/
│   ├── Day-10/
│   ├── Day-11/
│   ├── Day-12/
│   ├── Day-13/
│   ├── Day-14/
│   ├── Day-15/
│   ├── Day-16/
│   ├── Day-17/
│   ├── Day-18/
│   ├── Day-19/
│   └── Day-20/
│
└── README.md
```

## Skills Developed

Through these hands-on exercises, I practised:

- Python programming fundamentals.
- Linux command-line operations.
- Security log processing.
- Authentication monitoring.
- Failed login detection.
- Cloud IAM security concepts.
- JSON, CSV and YAML processing.
- Basic security risk assessment.
- Automated security reporting.
- Python exception handling.
- Security scripting and automation.

## Career Relevance

This learning journey supports my preparation for entry-level roles such as:

- Cloud Support Engineer
- Cloud Support Associate
- Junior Cloud Engineer
- Junior Cloud Security Analyst
- Cloud Operations Associate
- SOC Analyst – Tier 1

## Learning Status

**20 Days of Python Cloud Security Practice Completed**

This repository represents my hands-on learning and practical implementation of Python programming concepts applied to cloud security scenarios.

I will continue expanding this repository with more advanced Python scripting, cloud security automation, AWS and Azure integrations, and practical security projects.

---

**Author:** Sri Gayathri Rachuri

**GitHub:** https://github.com/srirachuri/cloud-security-projects

**Focus Areas:** Python | Cloud Security | AWS | Azure | Linux | Security Automation
