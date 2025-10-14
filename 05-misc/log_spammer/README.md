# log_spammer — Generate noisy log lines

A tiny utility that continuously prints synthetic log lines to stdout (and optionally appends them to a file). Useful to:

- Stress test log ingestion
- Create noisy background for detection testing
- Generate datasets for parsing and correlation labs

## Requirements

```
Python 3.8+ (no external libraries)
```

## Usage

Infinite stream at 5 lines/second:

```
python3 spam_logs.py -r 5
```

Generate 1000 lines into `sim.log` at 20 lines/sec:

```
python3 spam_logs.py -r 20 -n 1000 -o sim.log
```

## Notes

- Log format is simple and synthetic: timestamp, level, source, src IP, message.
- Use this to simulate noisy environments where bad signals are hidden in legitimate traffic.