#!/usr/bin/python3
"""
Reads from stdin line by line and computes metrics.

This script reads input from standard input (stdin) line by line and computes
metrics such as total file size, count of different HTTP status codes, and total
number of lines processed.

Metrics computed:
- Total file size: Sum of file sizes extracted from each line.
- HTTP status code count: Counts the occurrence of different HTTP status codes.
- Total line count: Total number of lines processed.

Usage:
    This script is intended to be run from the command line. It reads input from
    standard input (stdin) and prints metrics to standard output (stdout).

    Example usage:
    $ cat access.log | python3 script.py

    The script reads lines from the access.log file (or any other input passed
    via stdin) and prints computed metrics to stdout.
"""
import sys
from collections import defaultdict

total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) >= 5:
            status_code = parts[-2]
            file_size = int(parts[-1])

            total_file_size += file_size
            status_code_count[status_code] += 1
            line_count += 1

            if line_count % 10 == 0:
                print(f"Total file size: {total_file_size}")
                for code in sorted(status_code_count.keys()):
                    if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
                        print(f"{code} : {status_code_count[code]}")
                print()
except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_count.keys()):
        if code in ['200', '301', '400', '401', '403', '404', '405', '500']:
            print(f"{code} : {status_code_count[code]}")

