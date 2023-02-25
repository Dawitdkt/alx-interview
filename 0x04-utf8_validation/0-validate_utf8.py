#!/usr/bin/python3
"""some doc """


def validUTF8(data):
    """method doc"""
    # Initialize a variable to store the number of bytes to process
    n_bytes = 0

    # Iterate over each integer in the data list
    for num in data:

        # Get the binary representation of the least significant 8 bits
        bin_rep = format(num, '#010b')[-8:]

        # If this is the first byte
        if n_bytes == 0:

            # Count how many consecutive 1s are in the most significant bits
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            if n_bytes == 0:
                continue
            elif n_bytes == 1 or n_bytes > 4:
                return False

        # If this is a subsequent byte
        else:

            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        # Decrease the number of bytes to process by one
        n_bytes -= 1

    # Return True if there are no remaining bytes to process, otherwise False
    return n_bytes == 0
