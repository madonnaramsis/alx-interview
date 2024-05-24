#!/usr/bin/python3
"""
This module contains a function for validating UTF-8 encoding.

The function `validUTF8` takes a data set as input
and determines if it represents a valid UTF-8 encoding.
It checks each element in the data set
and verifies if it follows the UTF-8 encoding rules.

Example usage:
    data = [197, 130, 1]  # Represents the UTF-8 encoding for the character 'Ç'
    result = validUTF8(data)
    print(result)  # Output: True
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

    Args:
        data (list): The data set to be checked for UTF-8 encoding.

    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
                False otherwise.
    """
    num_bytes = 0

    for num in data:
        byte = format(num, '#010b')[-8:]

        if num_bytes == 0:
            for bit in byte:
                if bit == '0':
                    break
                num_bytes += 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte[0] == '1' and byte[1] == '0'):
                return False

        num_bytes -= 1

    return num_bytes == 0
