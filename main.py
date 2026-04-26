## Will encrypt and decrypt the message ## 

import sys

from aes.sBox import subByte, generateInvSBox
from aes.mixColumns import mixColumns, invMixColumns, shiftRows, invShiftRows
from aes.keyExpansion import keyExpansion
from aes.helperFunctions import printStateBox, printRoundKeys, printEncryptionProcess


def make_key(key_string):
    key = [ord(c) for c in key_string[:16]]

    while len(key) < 16:
        key.append(0x20)

    return key


def bytes_to_state(byte_list):
    state = [[0 for _ in range(4)] for _ in range(4)]

    for i in range(16):
        row = i % 4
        col = i // 4
        state[row][col] = byte_list[i]

    return state


def state_to_bytes(state):
    output = []

    for col in range(4):
        for row in range(4):
            output.append(state[row][col])

    return output


def addRoundKey(state, round_key):
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            new_state[r][c] = state[r][c] ^ round_key[r][c]

    return new_state


def subBytes(state):
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            new_state[r][c] = subByte(state[r][c])

    return new_state


def invSubBytes(state):
    inv_sbox = generateInvSBox()
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    for r in range(4):
        for c in range(4):
            byte = state[r][c]
            new_state[r][c] = inv_sbox[byte // 16][byte % 16]

    return new_state


def make_round_keys(key_bytes):
    round_keys = []

    current_key = bytes_to_state(key_bytes)
    round_keys.append(current_key)

    for round_count in range(1, 11):
        current_key = keyExpansion(current_key, round_count)
        round_keys.append(current_key)

    return round_keys


def encrypt_block(block, round_keys):
    state = bytes_to_state(block)

    state = addRoundKey(state, round_keys[0])

    for round_num in range(1, 10):
        state = subBytes(state)
        state = shiftRows(state)
        state = mixColumns(state)
        state = addRoundKey(state, round_keys[round_num])

    state = subBytes(state)
    state = shiftRows(state)
    state = addRoundKey(state, round_keys[10])

    return state_to_bytes(state)


def decrypt_block(block, round_keys):
    state = bytes_to_state(block)

    state = addRoundKey(state, round_keys[10])

    for round_num in range(9, 0, -1):
        state = invShiftRows(state)
        state = invSubBytes(state)
        state = addRoundKey(state, round_keys[round_num])
        state = invMixColumns(state)

    state = invShiftRows(state)
    state = invSubBytes(state)
    state = addRoundKey(state, round_keys[0])

    return state_to_bytes(state)


def encrypt_file(key_string, input_file, output_file):
    key_bytes = make_key(key_string)
    round_keys = make_round_keys(key_bytes)

    with open(input_file, "rb") as f:
        data = list(f.read())

    while len(data) % 16 != 0:
        data.append(0x20)

    encrypted_data = []

    for i in range(0, len(data), 16):
        block = data[i:i + 16]
        encrypted_data.extend(encrypt_block(block, round_keys))

    with open(output_file, "wb") as f:
        f.write(bytes(encrypted_data))

    print("Encryption complete.")


def decrypt_file(key_string, input_file, output_file):
    key_bytes = make_key(key_string)
    round_keys = make_round_keys(key_bytes)

    with open(input_file, "rb") as f:
        data = list(f.read())

    decrypted_data = []

    for i in range(0, len(data), 16):
        block = data[i:i + 16]

        if len(block) == 16:
            decrypted_data.extend(decrypt_block(block, round_keys))

    with open(output_file, "wb") as f:
        f.write(bytes(decrypted_data))

    print("Decryption complete.")


def main():
    if len(sys.argv) != 5:
        print('Usage:')
        print('python main.py encrypt "0123456789abcdef" input.txt output.txt')
        print('python main.py decrypt "0123456789abcdef" output.txt recovered.txt')
        return

    mode = sys.argv[1]
    key_string = sys.argv[2]
    input_file = sys.argv[3]
    output_file = sys.argv[4]

    if mode == "encrypt":
        encrypt_file(key_string, input_file, output_file)
    elif mode == "decrypt":
        decrypt_file(key_string, input_file, output_file)
    else:
        print("Mode must be encrypt or decrypt.")


if __name__ == "__main__":
    main()