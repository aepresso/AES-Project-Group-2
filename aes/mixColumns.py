## This holds the mixColumns, shiftRows, and their inverse functions and assigned to Ryan K ##

from aes.helperFunctions import polyMultiply


def mixColumns(state):
    """
    This performs the AES Mix Columns step for encryption.
    """
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for c in range(4):
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]

        new_state[0][c] = polyMultiply(0x02, s0) ^ polyMultiply(0x03, s1) ^ s2 ^ s3
        new_state[1][c] = s0 ^ polyMultiply(0x02, s1) ^ polyMultiply(0x03, s2) ^ s3
        new_state[2][c] = s0 ^ s1 ^ polyMultiply(0x02, s2) ^ polyMultiply(0x03, s3)
        new_state[3][c] = polyMultiply(0x03, s0) ^ s1 ^ s2 ^ polyMultiply(0x02, s3)

    return new_state


def invMixColumns(state):
    """
    This performs the AES Inverse Mix Columns step for decryption.
    """
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for c in range(4):
        s0 = state[0][c]
        s1 = state[1][c]
        s2 = state[2][c]
        s3 = state[3][c]

        new_state[0][c] = polyMultiply(0x0e, s0) ^ polyMultiply(0x0b, s1) ^ polyMultiply(0x0d, s2) ^ polyMultiply(0x09, s3)
        new_state[1][c] = polyMultiply(0x09, s0) ^ polyMultiply(0x0e, s1) ^ polyMultiply(0x0b, s2) ^ polyMultiply(0x0d, s3)
        new_state[2][c] = polyMultiply(0x0d, s0) ^ polyMultiply(0x09, s1) ^ polyMultiply(0x0e, s2) ^ polyMultiply(0x0b, s3)
        new_state[3][c] = polyMultiply(0x0b, s0) ^ polyMultiply(0x0d, s1) ^ polyMultiply(0x09, s2) ^ polyMultiply(0x0e, s3)

    return new_state


def shiftRows(state):
    """
    This performs the AES Shift Rows step for encryption.
    """
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            new_state[r][c] = state[r][(c + r) % 4]

    return new_state


def invShiftRows(state):
    """
    This performs the AES Inverse Shift Rows step for decryption.
    """
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            new_state[r][(c + r) % 4] = state[r][c]

    return new_state