# *Go Through the Attached pdf file for screenshots*

# ASW-MSCAN 🛡️
Malicious File Scanner (asw_mscan) – Built a Python-based malware scanner that generates file hashes and compares them against known malicious hash datasets (VirusShare). Packaged into an executable for cross-platform use.

# Overview

**"asw_mscan"** is an educational malware detection tool that scans files and checks whether they match known malicious hashes from a dataset (e.g., VirusShare). If a match is found, the file is flagged as potentially malicious.

This project demonstrates how hash-based malware detection works, a foundational concept in cybersecurity.

# Features

🔍 File scanning – Generate MD5/SHA256 hashes of files.

📂 Batch scanning – Scan all files in a directory.

⚡ Hash comparison – Check file hashes against a malicious hash dataset.

🖥️ CLI support – Run directly in the terminal.

🧪 Educational use – Designed for learning and research, not real-world AV replacement.

# Safety Note 🔒 

This project is for educational purposes only.
Do not use it on real systems without proper isolation (VMs, sandboxes).

# Installation 📦
**Option 1 – Run with Python**

Clone the repository:

git clone https://github.com/your-username/asw_mscan.git
cd asw_mscan

Run The Script:

python3 asw_mscan.py

**Option 2 – Run as Executable**

If you built the executable with PyInstaller:

./dist/asw_mscan

# Usage
It is pretty simple to use.
After execution of the script, inside the terminal you will be promted to Enter your File, you will have to choose your sample for testing.

Then, Choose a database of malicious Hashes that you want to compare and match.

Now the script will generate a hash of your sample malicious file and match it with the database and give you the result.


# Future Improvements

Integrate YARA rules for pattern-based detection.

Add real-time scanning capability.

Provide GUI frontend for easier use.
