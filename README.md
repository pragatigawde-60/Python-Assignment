# Python-Assignment
# Q1 Password Strength Checker (DevOps Security)

## 📌 Project Overview
In DevOps, security is a critical responsibility, and strong passwords play a key role in protecting systems and applications.  
This project implements a **Python-based Password Strength Checker** that validates user passwords against common security best practices.
The script checks whether a password meets predefined strength criteria and provides clear feedback to the user.

## 🎯 Objective
- To create a Python function that evaluates password strength.
- To enforce commonly accepted password security standards.
- To provide meaningful feedback to users for improving weak passwords.

## 🛠️ Features
The password is validated against the following criteria:

- ✅ Minimum length of **8 characters**
- ✅ Contains **at least one uppercase letter (A–Z)**
- ✅ Contains **at least one lowercase letter (a–z)**
- ✅ Contains **at least one digit (0–9)**
- ✅ Contains **at least one special character**  
  (`! @ # $ % ^ & * ( ) _ + - =` etc.)

## 🧩 Function Description

### `check_password_strength(password)`
- **Input:**  
  - `password` (string)
- **Output:**  
  - `True` → Password meets all criteria  
  - `False` → Password does not meet one or more criteria

This function performs validation using Python string methods and character checks.

## 📂 Project Structure
password-strength-checker/
│
├── password_strength_checker.py
└── README.md

## Run the script and Output is here:
Weak password:
<img width="581" height="121" alt="image" src="https://github.com/user-attachments/assets/37eb6354-59ca-4e37-bdde-738bf399c804" />

Strong password:
<img width="597" height="70" alt="image" src="https://github.com/user-attachments/assets/d5f2c4d4-c341-4092-beda-b924973181d1" />



# Q2 CPU Health Monitoring Tool 

## 📌 Project Overview
Monitoring server health is a critical responsibility of a DevOps engineer. This project implements a **Python-based CPU Health Monitoring tool** that continuously tracks CPU usage of the local machine and raises alerts when usage exceeds a defined threshold.

The program runs indefinitely and provides real-time alerts, simulating a basic system monitoring mechanism used in production environments.

## 🎯 Objective
- To continuously monitor CPU utilization
- To display alerts when CPU usage exceeds a predefined threshold
- To demonstrate proactive monitoring practices in DevOps
- To handle runtime exceptions gracefully

## 🛠️ Features
- 🔄 Continuous CPU monitoring
- 🚨 Alert generation when CPU usage exceeds threshold (default: **80%**)
- ⏳ Runs indefinitely until manually interrupted
- ⚠️ Robust error handling to prevent unexpected crashes

## 📚 Technologies Used
- **Python 3**
- **psutil** library for system metrics


## 📦 Prerequisites

### Install Python cy
```bash
pip install psutil

🧩 Program Logic

The program uses psutil.cpu_percent() to fetch CPU usage.
CPU usage is checked at regular intervals.
If usage exceeds the defined threshold:
An alert message is displayed.
The program continues running until interrupted using Ctrl + C.
Exception handling ensures stability during runtime.

📂 Project Structure
cpu-health-monitor/
│
├── CPU_threshold_Checker.py
└── README.md

# Run the script and Output is here:
<img width="581" height="198" alt="image" src="https://github.com/user-attachments/assets/7e6fb452-3b2c-418e-adb2-e429aebd99f7" />



## Q4 File Backup Automation Script

## 📌 Project Overview
Regular backups are a critical part of DevOps and system reliability practices. This project implements a **Python-based file backup script** that copies files from a source directory to a destination directory while ensuring file name uniqueness using timestamps.

The script is designed to be executed from the command line and includes robust error handling for common failure scenarios.


## 🎯 Objective
- To automate file backups using Python
- To prevent file overwrites by appending timestamps
- To handle missing directories gracefully
- To demonstrate basic backup and recovery concepts in DevOps


## 🛠️ Features
- 📁 Copies all files from source to destination directory
- ⏱️ Automatically appends a timestamp if a file already exists
- ⚠️ Graceful error handling for invalid directories
- 💻 Command-line execution support


## 📚 Technologies Used
- **Python 3**
- Standard Python libraries:
  - `os`
  - `shutil`
  - `sys`
  - `datetime`

## 📂 Project Structure

file-backup-script/
│
├── Backupnew.py
└── README.md

2️⃣ Run the Backup 
python backup.py /path/to/source /path/to/destination
Replace:
/path/to/source → directory containing files to back up
/path/to/destination → directory where backups will be stored







