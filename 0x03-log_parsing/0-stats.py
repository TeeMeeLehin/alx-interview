#!/usr/bin/python3
"""log parsing script"""
import re
import sys
from collections import Counter

pattern = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - ' \
            r'\[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'
pattern = re.compile(pattern)
count = 0
total_fs = 0
status_codes = []

try:
    for line in sys.stdin:
        if pattern.match(line):
            count += 1
            line = line.strip()
            deets = line.split('"')[2]
            deets = deets.strip()
            status_code = int(deets.split()[0])
            file_size = int(deets.split()[1])

            status_codes.append(status_code)
            total_fs += file_size

            if count % 10 == 0:
                print("File size: {}".format(total_fs))
                status_codes = sorted(status_codes)
                s_c = Counter(status_codes)

                for key, value in s_c.items():
                    print("{}: {}".format(key, value))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_fs))
    status_codes = sorted(status_codes)
    s_c = Counter(status_codes)

    for key, value in s_c.items():
        print("{}: {}".format(key, value))
