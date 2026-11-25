#!/usr/bin/env python3
"""Count failed SSH logins per IP from a Linux auth log and flag likely brute force.

Usage: python3 analyze_auth.py sample_auth.log [threshold]
"""
import re
import sys
from collections import Counter

PATTERN = re.compile(r"Failed password for (?:invalid user )?(\S+) from (\d+\.\d+\.\d+\.\d+)")


def main():
    path = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    by_ip, by_user = Counter(), Counter()
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            m = PATTERN.search(line)
            if m:
                by_user[m.group(1)] += 1
                by_ip[m.group(2)] += 1
    print("Failed logins per IP:")
    for ip, n in by_ip.most_common():
        flag = "  <-- possible brute force" if n >= threshold else ""
        print(f"  {ip}: {n}{flag}")
    print("Most targeted usernames:")
    for user, n in by_user.most_common(5):
        print(f"  {user}: {n}")


if __name__ == "__main__":
    main()
