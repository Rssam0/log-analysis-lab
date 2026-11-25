# Log analysis lab

A small Python script that reads a Linux `auth.log` and counts failed SSH logins per IP address. It flags IPs above a threshold as possible brute force attempts.

The sample log is made up (documentation IP ranges), so no real data is involved.

## Run
```
python3 analyze_auth.py sample_auth.log 5
```

## What I learned
- SOC analysts spend a lot of time reading logs, so being able to count and group events matters.
- Repeated failures from one IP against "admin" or "root" is a classic brute-force pattern.
- Limits: this only looks at one log format and one pattern. A real tool would also check for a successful login after many failures, and watch for slow attacks.

## Next steps
- Add detection of "many failures then a success"
- Output a CSV
- Try the same idea on Windows event logs (event ID 4625 = failed logon)
