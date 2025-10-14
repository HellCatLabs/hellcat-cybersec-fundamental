# dns_resolver — Simple DNS resolver

A compact CLI to resolve domains to IP addresses and optionally perform reverse PTR lookups. Useful to verify DNS behavior, generate test data, or demonstrate lookup anomalies.

## Requirements

```
Python 3.x (built-in socket module)
```

## Usage

Resolve one or more domains:

```
python3 resolve.py example.com api.example.org
```

Resolve and perform reverse PTR lookup:

```
python3 resolve.py example.com --reverse
```

## Notes

- Uses system DNS resolver (no external dependencies).
- Use this to produce DNS-resolution-based logs or to test detection rules related to suspicious domains.