import hashlib
import os
import sys

def calculate_md5(filepath):
    """
    Calculates the MD5 hash of a file.
    Designed to handle large files by reading in chunks.
    """
    md5_hash = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5_hash.update(chunk)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        return None
    except IOError:
        print(f"Error: Could not read file {filepath}")
        return None

def load_malicious_hashes(hash_file):
    """
    Loads malicious MD5 hashes from a file into a set for quick lookups.
    """
    malicious_hashes = set()
    try:
        with open(hash_file, "r") as f:
            for line in f:
                malicious_hashes.add(line.strip().lower())  # lowercase to match format
        print(f"Loaded {len(malicious_hashes)} malicious hashes from {hash_file}.")
        return malicious_hashes
    except FileNotFoundError:
        print(f"Error: Hash database file '{hash_file}' not found.")
        return None

def main():
    """
    Interactive malware scanner using MD5 hashes.
    """
    print(r"""
 █████╗ ███████╗██╗    ██╗      ███╗   ███╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔══██╗██╔════╝██║    ██║      ████╗ ████║██╔════╝██╔════╝██╔══██╗████╗  ██║
███████║███████╗██║ █╗ ██║█████╗██╔████╔██║███████╗██║     ███████║██╔██╗ ██║
██╔══██║╚════██║██║███╗██║╚════╝██║╚██╔╝██║╚════██║██║     ██╔══██║██║╚██╗██║
██║  ██║███████║╚███╔███╔╝      ██║ ╚═╝ ██║███████║╚██████╗██║  ██║██║ ╚████║
╚═╝  ╚═╝╚══════╝ ╚══╝╚══╝       ╚═╝     ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"asw_mscan" is a lightweight Python-based malware detection tool. 
It allows users to scan files by generating their cryptographic hash (MD5/SHA256) and comparing it against a dataset of known malicious file hashes (e.g., from VirusShare). 
If a match is found, the file is flagged as malicious.
The project is designed for educational and research purposes, helping students and beginners understand how basic malware detection using hash-matching works.

""")

    file_to_scan = input("Enter file to scan: ").strip()
    hash_database_file = input("Enter hash database file: ").strip()

    malicious_hashes = load_malicious_hashes(hash_database_file)
    if not malicious_hashes:
        sys.exit(1)

    if not os.path.isfile(file_to_scan):
        print(f"Error: '{file_to_scan}' is not a valid file.")
        sys.exit(1)

    target_hash = calculate_md5(file_to_scan)
    if target_hash is None:
        print("Scan failed.")
        sys.exit(1)

    if target_hash in malicious_hashes:
        print(f"\n[!] ALERT: '{file_to_scan}' is MALICIOUS!")
        print(f"    MD5: {target_hash}")
    else:
        print(f"\n[+] SAFE: '{file_to_scan}' appears clean.")
        print(f"    MD5: {target_hash}")

if __name__ == "__main__":
    main()
