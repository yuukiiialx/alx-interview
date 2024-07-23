#!/usr/bin/python3
"""
0-validate_utf8 module
"""


def validUTF8(data) -> bool:
    """Determines if a given data set represents a valid UTF-8 encoding"""

    def byte_sequence_count(byte):
        """Returns the number of bytes in a UTF-8 sequence"""
        leading_ones = 0
        while (byte >> 7 - leading_ones) & 1:
            leading_ones += 1
        return leading_ones

    i = 0
    # 11000010 10000000 11000010 10000000
    # 01000010
    while i < len(data):
        sequence_count = byte_sequence_count(data[i])

        if sequence_count == 0:
            i += 1
            continue

        if sequence_count == 1 or sequence_count > 4:
            return False

        if i + sequence_count > len(data):
            return False
        # 11000010 10000000
        for j in range(1, sequence_count):
            if not (data[i + j] >> 6 == 0b10):
                return False

        i += sequence_count

    return True
