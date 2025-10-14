# fake_usergen — Generate Fake Users CSV

This small script creates a CSV file containing fake user accounts (username, email, plaintext password for testing, hashed password, created timestamp). Useful to populate test databases, SIEM ingestion pipelines, or demo dashboards.


## Requirements

``` 
Python 3.8+ (no external libs)
```

## Usage

```
python3 generate_users.py -o fake_users.csv -n 200
```

This will produce `fake_users.csv` with 200 entries.


## Fields

- username
- email
- password_plain (for testing; remove for real use)
- password_hash (SHA256)
- created_at (UTC ISO8601)

## Ideas

- Remove `password_plain` when exporting to production-like datasets.
- Feed CSV into your ingest pipeline to test detection rules (e.g., unusual volumes of new accounts).
- Use as data for credential stuffing simulations (in a safe lab).