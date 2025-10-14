# 📁 File Operations — "Dropper" Basics

In this lab, you’ll create a simple Python script that writes a file to disk — mimicking what many malware samples do when they drop payloads or markers on a system.

## Goal

Understand how to:
- Write and create files in Python
- Simulate a basic "dropper" behavior
- Prepare for future labs involving persistence or payload deployment

## Why it matters

Malware and other tools often:
- Drop executables, scripts, or DLLs
- Leave logs or flag files to track execution
- Modify or overwrite system files

Knowing how file creation works is **essential for detection, analysis, and malware development**.


## What the script does

The provided script:
- Creates a file called `dropped.txt`
- Writes a test message inside
- Saves it in the current folder

## Run it:

```bash
python3 file_dropper.py
```

Check that the file was created:

```sh
cat dropped.txt
```

## Bonus ideas

Try modifying the script to:
- Drop the file in a specific location (e.g. `/tmp/`, `C:\\Users\\user\\AppData\\`)
- Write binary data instead of text
- Append to an existing file
- Randomize file names


## Blue Team Note

Dropped files can:
- Be detected by EDR or antivirus tools
- Leave forensic traces (timestamps, content, location)
- Trigger alerts when written to suspicious paths (like AppData, Startup, etc.)

Understanding how and where files are dropped helps defenders build better detection rules.
