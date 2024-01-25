#!/usr/bin/python3
import re
import sys
import signal
from collections import Counter

pattern = re.compile(r'^(\d+\.\d+\.\d+\.\d+) - \[(.+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$')

count = 0
total_fs = 0
status_codes = []

def signal_handler(sig, frame):
    global total_fs
    global status_codes
    
    print("File size: {}".format(total_fs))
    status_codes = sorted(status_codes)
    s_c = Counter(status_codes)

    for key, value in s_c.items():
        print("{}: {}".format(key, value))
    sys.exit(0)
    
signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    if pattern.match(line):
        count += 1
        line = line.strip()
        deets = line.split('"')[2]
        deets = deets.strip()
        status_code = deets.split()[0]
        file_size = int(deets.split()[1])

        status_codes.append(status_code)
        total_fs += file_size

        if count == 10:
            print("File size: {}".format(total_fs))
            status_codes = sorted(status_codes)
            s_c = Counter(status_codes)

            for key, value in s_c.items():
                print("{}: {}".format(key, value))

    else:
        pass

        
    
    
            
