## This holds the mixColumns, shiftRows, and their inverse functions and assigned to Ryan K ##

## This will hold the mixColumns function and assigned to Ryan K ##

from helperFunctions import gfMultiply


def mixColumns(state):
    """
    This performs the AES Mix Columns step for encryption.
    It takes each column of the state box and multiplies it
    by the AES Mix Columns matrix.

    Args:
        state: a 4x4 array of byte values

    Returns:
        a new 4x4 state after Mix Columns is applied
    """
    new_state = [[0 for i in range(4)] for j in range(4)]

    for c in range(4):
        # Save the current column values
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]

        # Apply the AES Mix Columns matrix
        new_state[0][c] = gfMultiply(0x02, s0) ^ gfMultiply(0x03, s1) ^ s2 ^ s3
        new_state[1][c] = s0 ^ gfMultiply(0x02, s1) ^ gfMultiply(0x03, s2) ^ s3
        new_state[2][c] = s0 ^ s1 ^ gfMultiply(0x02, s2) ^ gfMultiply(0x03, s3)
        new_state[3][c] = gfMultiply(0x03, s0) ^ s1 ^ s2 ^ gfMultiply(0x02, s3)

    return new_state


def invMixColumns(state):
    """
    This performs the AES Inverse Mix Columns step for decryption.
    It reverses the normal Mix Columns operation by using the
    inverse AES Mix Columns matrix.

    Args:
        state: a 4x4 array of byte values

    Returns:
        a new 4x4 state after Inverse Mix Columns is applied
    """
    new_state = [[0 for i in range(4)] for j in range(4)]

    for c in range(4):
        # Save the current column values
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]

        # Apply the AES Inverse Mix Columns matrix
        new_state[0][c] = gfMultiply(0x0e, s0) ^ gfMultiply(0x0b, s1) ^ gfMultiply(0x0d, s2) ^ gfMultiply(0x09, s3)
        new_state[1][c] = gfMultiply(0x09, s0) ^ gfMultiply(0x0e, s1) ^ gfMultiply(0x0b, s2) ^ gfMultiply(0x0d, s3)
        new_state[2][c] = gfMultiply(0x0d, s0) ^ gfMultiply(0x09, s1) ^ gfMultiply(0x0e, s2) ^ gfMultiply(0x0b, s3)
        new_state[3][c] = gfMultiply(0x0b, s0) ^ gfMultiply(0x0d, s1) ^ gfMultiply(0x09, s2) ^ gfMultiply(0x0e, s3)

    return new_state


def shiftRows(state):
    """
    This performs the AES Shift Rows step for encryption.
    Row 0 does not move, row 1 shifts left by 1,
    row 2 shifts left by 2, and row 3 shifts left by 3.

    Args:
        state: a 4x4 array of byte values

    Returns:
        a new 4x4 state after Shift Rows is applied
    """
    new_state = [[0 for i in range(4)] for j in range(4)]

    for r in range(4):
        for c in range(4):
            # Shift each row left by its row number
            new_state[r][c] = state[r][(c + r) % 4]

    return new_state


def invShiftRows(state):
    """
    This performs the AES Inverse Shift Rows step for decryption.
    Row 0 does not move, row 1 shifts right by 1,
    row 2 shifts right by 2, and row 3 shifts right by 3.

    Args:
        state: a 4x4 array of byte values

    Returns:
        a new 4x4 state after Inverse Shift Rows is applied
    """
    new_state = [[0 for i in range(4)] for j in range(4)]

    for r in range(4):
        for c in range(4):
            # Shift each row right by its row number
            new_state[r][(c + r) % 4] = state[r][c]

    return new_state