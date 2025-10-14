# 🧪 05 - Exercises & Mini Challenges

Time to test what you’ve learned so far.

This folder contains **mini-projects and exercises** based on the previous labs:
- Command execution
- File writing
- MAC spoofing
- Basic system inspection

You can do them in **any order**. Try solving them on your own before looking anything up.  
You don’t need fancy code — just working logic.


## Instructions

For each exercise:

- Create a new Python file (e.g. `exo1.py`)
- Add a comment with the name of the exercise
- Solve it using what you’ve learned
- Bonus: Try on both Linux and Windows when possible

## Exercises

### 1. Who Are You, Really?

> Create a script that prints:
> - Current username
> - Hostname
> - The user’s home directory

### 2. Drop-and-Append

> Write a script that:
> - Creates a file named `report.log`
> - Appends a new line each time it runs: e.g., "Run at [timestamp]"

Bonus: add the user and hostname on the same line.

### 3. MAC Address Randomizer (Linux only)

> Write a script that:
> - Brings down the network interface `eth0`
> - Sets a random MAC address (generate it)
> - Brings the interface back up

💡 Tip: Use `random` and `ifconfig`.


### 4. Drop in Hidden Location

> Drop a file in a hidden folder:
> - Linux: `~/.config/`
> - Windows: `%APPDATA%` or `Startup`

File content can be anything. The goal is just to control the location.

### 5. Stealth Dropper (Hard)

> Write a script that:
> - Generates a random filename
> - Writes a binary payload (`b"\x90\x90\x90\xcc"`)
> - Saves it in the temp folder
> - Logs the full path in `~/.hellcat_log`

## Bonus

If you finish these, try writing your **own lab** using what you’ve learned.  
Feel free to contribute it back to the repo!

### Reminder

These exercises are meant for **educational purposes only**.  
Always work in a sandbox, and never run unknown scripts on your main machine.

Have fun — and don’t forget to break things on purpose.