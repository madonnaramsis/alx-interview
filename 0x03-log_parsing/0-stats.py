#!/usr/bin/python3
"""
This script processes log data from standard input, calculating metrics
like total file size and HTTP status code counts. It prints reports every
10 lines and a final report at the end.
"""

import sys


status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
line_counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])
            if status_code in status_codes.keys():
                status_codes[status_code] += 1
            total_file_size += file_size
            line_counter += 1
        if line_counter == 10:
            line_counter = 0
            print('Total file size: {}'.format(total_file_size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))
except Exception as err:
    pass
finally:
    print('Total file size: {}'.format(total_file_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
