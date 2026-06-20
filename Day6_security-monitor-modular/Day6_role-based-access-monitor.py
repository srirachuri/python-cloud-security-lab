# Role-Based Access Monitor

A Python cybersecurity project that evaluates user access permissions based on assigned roles and generates an access report using a modular design.

## Project Overview

This project simulates a simple Role-Based Access Control (RBAC) system used in cloud and enterprise environments.

The application determines a user's access level based on their role and generates an access report.

Supported roles include:

- Admin
- Security
- Developer
- User (Default)

## Technologies Used

- Python 3
- Ubuntu Linux
- VirtualBox

## Features

- Modular Python design
- Custom modules and imports
- User role validation
- Access level classification
- Access reporting
- Security-focused authorization logic

## Module: access_utils.py

```
def check_access(role):

    if role == "admin":
        return "FULL ACCESS"

    elif role == "security":
        return "SECURITY ACCESS"

    elif role == "developer":
        return "LIMITED ACCESS"

    else:
        return "ACCESS DENIED"
```

## Main Program: access_monitor.py

```
from access_utils import check_access

username = input("Enter Username: ")
role = input("Enter Role: ")

access = check_access(role)

print("\n--- ACCESS REPORT ---")
print("Username:", username)
print("Role:", role)
print("Access Level:", access)
```

## Sample Output

### User Role

```
Enter Username: Sri
Enter Role: User

--- ACCESS REPORT ---
Username: Sri
Role: User
Access Level: ACCESS DENIED
```

### Developer Role

```
Enter Username: Sri Gayathri
Enter Role: developer

--- ACCESS REPORT ---
Username: Sri Gayathri
Role: developer
Access Level: LIMITED ACCESS
```

### Security Role

```
Enter Username: Gayathri
Enter Role: security

--- ACCESS REPORT ---
Username: Gayathri
Role: security
Access Level: SECURITY ACCESS
```

### Admin Role

```
Enter Username: SRI GAYATHRI
Enter Role: admin

--- ACCESS REPORT ---
Username: SRI GAYATHRI
Role: admin
Access Level: FULL ACCESS
```

## Learning Objectives

This project helped me practice:

- Python Functions
- Modules and Imports
- User Input Handling
- Conditional Logic
- Access Control Concepts
- Security Reporting

## Cybersecurity Relevance

Role-Based Access Control (RBAC) is widely used in:

- AWS IAM
- Azure RBAC
- Google Cloud IAM
- Enterprise Identity Management
- Security Operations Centres (SOC)

RBAC helps organisations enforce the Principle of Least Privilege by granting users only the permissions required for their role.

## Skills Demonstrated

- Python Fundamentals
- Modular Programming
- Access Control Logic
- Security Automation Basics
- Code Reusability
- Authorization Concepts

## Future Improvements

- Add multiple permission levels
- Support custom roles
- Store users in a file or database
- Add login authentication
- Generate audit logs
- Create role management features

## Author

Sri Gayathri

Aspiring Cloud Security Engineer | Cybersecurity Student
