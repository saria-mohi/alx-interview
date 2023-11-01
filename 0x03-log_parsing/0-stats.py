#!/usr/bin/python3

import sys


def print_message(status_code_counts, total_file_size):
    """
    Method to print
    Args:
        status_code_counts: Dictionary of status codes
        total_file_size: Total size of the file
    Returns:
        Nothing
    """

    print("File size: {}".format(total_file_size))
    for code, count in sorted(status_code_counts.items()):
        if count != 0:
            print("{}: {}".format(code, count))


status_code_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                      '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
counter = 0

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line
        parsed_line = parsed_line[::-1]  # Reverse the order of elements

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                total_file_size += int(parsed_line[0])  # Extract file size
                status_code = parsed_line[1]  # Extract status code

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

            if counter == 10:
                print_message(status_code_counts, total_file_size)
                counter = 0

finally:
    print_message(status_code_counts, total_file_size)