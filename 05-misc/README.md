# 🧩 05 - Miscellaneous Scripts

This section includes small but useful scripts that don't fit directly in malware, network, or keylogger labs.

Use these for:

- Simulating data
- Generating fake traffic
- Practicing basic Python scripting
- Building analysis datasets

## Included Labs

| Folder         | Description                              |
|----------------|------------------------------------------|
| fake_usergen/  | Generate fake user credentials (CSV)     |
| log_spammer/   | Create tons of fake log entries (for SOC testing) |
| dns_resolver/  | Simple DNS query script                  |

Each folder includes:
- A ready-to-run script
- A clear `README.md` with usage and ideas

## Related Modules

- **Use with malware labs**: Feed generated data into [03-malware-basics](../03-malware-basics) exfil and keylogger labs
- **Network testing**: Use `dns_resolver` alongside [02-network-ops](../02-network-ops) for reconnaissance practice
- **SOC training**: Use `log_spammer` and `fake_usergen` to populate SIEM pipelines, then write detection rules inspired by [04-keyloggers-trojans](../04-keyloggers-trojans)