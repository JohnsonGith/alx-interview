#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    print(f"File size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{status_code}: {count}")

line_count = 0
total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Check if the line has the expected format
        if len(parts) >= 10 and parts[-2].isnumeric():
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            # Update total size
            total_size += file_size

            # Update status code count
            if status_code in status_counts:
                status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_metrics(total_size, status_counts)

except KeyboardInterrupt:
    pass

print_metrics(total_size, status_counts)
