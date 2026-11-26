# Log analysis lab

A small python script that reads a linux `auth.log` and counts failed SSH logins per IP. Over the threshold, it flags the IP as possible brute force.

The sample log is made up (documentation IP ranges), nothing real in it.

Run it:
```
python3 analyze_auth.py sample_auth.log 5
```

What I got out of it:
- most of log work is just counting and grouping
- lots of failures from one IP against admin or root is the classic brute force shape
- this only reads one log format. a real tool would also catch "many failures then one success" and slow attacks that spread over days

Update: I made a Windows version of the same idea for event 4625, it's in the windows-4625-logon-parser repo.
