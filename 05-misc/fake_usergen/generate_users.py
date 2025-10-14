#!/usr/bin/env python3
"""
generate_users.py
Generate a CSV with fake users (username, email, password hash, created_at).
Purpose: create realistic-looking datasets for testing ingestion / detection pipelines.
"""

import csv
import random
import hashlib
import argparse
from datetime import datetime, timedelta

FIRST = ["alice", "bob", "carol", "dave", "eve", "mallory", "trent", "peggy", "oscar", "heidi"]
LAST = ["smith", "johnson", "williams", "brown", "jones", "miller", "davis", "garcia", "rodriguez"]
DOMAINS = ["example.com", "corp.local", "company.io", "mail.com", "service.net"]

def random_password(length=10):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_"
    return ''.join(random.choice(chars) for _ in range(length))

def hash_password(pw):
    # simple SHA256 hash for demo purposes
    return hashlib.sha256(pw.encode()).hexdigest()

def random_date(start_days_ago=365):
    start = datetime.utcnow() - timedelta(days=start_days_ago)
    delta = random.randint(0, start_days_ago)
    return (start + timedelta(days=delta)).isoformat() + "Z"

def gen_user():
    first = random.choice(FIRST)
    last = random.choice(LAST)
    num = random.randint(0, 9999)
    username = f"{first}.{last}{num}"
    domain = random.choice(DOMAINS)
    email = f"{first}.{last}{num}@{domain}"
    pwd = random_password(random.choice([8,10,12]))
    pwd_hash = hash_password(pwd)
    created = random_date(365*2)
    return {
        "username": username,
        "email": email,
        "password_plain": pwd,
        "password_hash": pwd_hash,
        "created_at": created
    }

def main(out_file, count):
    fieldnames = ["username","email","password_plain","password_hash","created_at"]
    with open(out_file, "w", newline="") as csvf:
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(count):
            writer.writerow(gen_user())
    print(f"[+] Generated {count} users -> {out_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate fake users CSV")
    parser.add_argument("-o", "--output", default="fake_users.csv", help="Output CSV filename")
    parser.add_argument("-n", "--number", type=int, default=100, help="Number of users to generate")
    args = parser.parse_args()
    main(args.output, args.number)