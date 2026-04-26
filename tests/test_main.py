from main import padKey, createStateBox, addRoundKey, subBytes, invSubBytes, encrypt, decrypt
import pytest
"""
This file tests the main function of this AES project
"""

def test_padKey():
    """
    Testing three cases:
    when the key is exactly 16 char
    when the key is too short
    when the key is too long 
    and when the key is wrong type
    """
    assert padKey("helloworldthisis") == b"helloworldthisis"
    assert padKey("helloworldthis") == b"helloworldthis  "
    assert padKey("helloworldthisisatesttoseeifitworks") == b"helloworldthisis"
    with pytest.raises(TypeError):
        padKey(12345)

def test_createStatebox():
    """
    Testins the create state box 
    with an easy bytes block
    """
    assert createStateBox([0x00, 0x01, 0x02, 0x03, 
                           0x04, 0x05, 0x06, 0x07, 
                           0x08, 0x09, 0x10, 0x11, 
                           0x12, 0x13, 0x14, 0x15]) == [
                                [0x00, 0x04, 0x08, 0x12],
                                [0x01, 0x05, 0x09, 0x13],
                                [0x02, 0x06, 0x10, 0x14],
                                [0x03, 0x07, 0x11, 0x15]
                           ]
def test_addRoundKey():
    """
    Testins addRoundKey functions to 
    check that it does xor the bytes correctly
    """
    testStateBox = [ 
        [0x01, 0x01,0x01,0x01],
        [0x01,0x01,0x01,0x01],
        [0x01,0x01,0x01,0x01],
        [0x01,0x01,0x01,0x01]
    ]
    testRoundKey = [
        [0xF1, 0xF1,0xF1,0xF1],
        [0xF1,0xF1,0xF1,0xF1],
        [0xF1,0xF1,0xF1,0xF1],
        [0xF1,0xF1,0xF1,0xF1]
    ]
    assert addRoundKey(testStateBox, testRoundKey) == [
        [0xF0,0xF0,0xF0,0xF0],
        [0xF0,0xF0,0xF0,0xF0],
        [0xF0,0xF0,0xF0,0xF0],
        [0xF0,0xF0,0xF0,0xF0]
    ]

def test_subBytes():
    """
    Tesing subBytes on a 4x4 matrix and making sure it works properly
    """
    testSimpleMatrix = [
        [0x00,0x00,0x00,0x00],
        [0xFF,0xFF,0xFF,0xFF],
        [0x00,0x00,0x00,0x00],
        [0xFF,0xFF,0xFF,0xFF]
    ]
    assert subBytes(testSimpleMatrix) == [
        [0x63,0x63,0x63,0x63],
        [0x16,0x16,0x16,0x16],
        [0x63,0x63,0x63,0x63],
        [0x16,0x16,0x16,0x16]
    ]

def test_invSubBytes(): 
    testSimpleMatrix = [
        [0x63,0x63,0x63,0x63],
        [0x16,0x16,0x16,0x16],
        [0x63,0x63,0x63,0x63],
        [0x16,0x16,0x16,0x16]
    ]
    
    assert invSubBytes(testSimpleMatrix) == [
        [0x00,0x00,0x00,0x00],
        [0xFF,0xFF,0xFF,0xFF],
        [0x00,0x00,0x00,0x00],
        [0xFF,0xFF,0xFF,0xFF]
    ]
def test_encrypt():
    # Key treated as ASCII string per assignment spec (Q-5)
    # Expected value verified from implementation output
    plaintext = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d,
                 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
    key = "2b7e151628aed2a6"
    result = encrypt(plaintext, key)
    assert result == [
        [0xFC, 0xE6, 0xAD, 0x96],
        [0x85, 0x8A, 0x18, 0x74],
        [0xAC, 0x0F, 0x0A, 0xEE],
        [0x50, 0x5C, 0xDE, 0x65]
    ]
    
    # readable plaintext and key
    plaintext = list("Hello, World!   ".encode('utf-8'))
    key = "supersecretkey"
    
    result = encrypt(plaintext, key)
    assert result == [
        [197, 162, 180, 203], [145, 121, 117, 26], [190, 216, 223, 110], [6, 1, 13, 4]
        ]
    
    # if key is a short key
    plaintext = [0x00] * 16
    key = "secret"  # 6 chars -> padded to "secret          "
    result = encrypt(plaintext, key)
    # Verify it runs without error and returns a 4x4 matrix
    assert len(result) == 4
    assert all(len(row) == 4 for row in result)
    assert all(0x00 <= b <= 0xFF for row in result for b in row)

def test_roundKeys():
    from main import generateAllRoundKeys
    keyMatrix = [
        [0x2b, 0x28, 0xab, 0x09],
        [0x7e, 0xae, 0xf7, 0xcf],
        [0x15, 0xd2, 0x15, 0x4f],
        [0x16, 0xa6, 0x88, 0x3c]
    ]
    roundKeys = generateAllRoundKeys(keyMatrix)
    assert roundKeys[1] == [
        [0xa0, 0x88, 0x23, 0x2a],
        [0xfa, 0x54, 0xa3, 0x6c],
        [0xfe, 0x2c, 0x39, 0x76],
        [0x17, 0xb1, 0x39, 0x05]
    ]
    
def test_decrypt():
    # Roundtrip test 1: binary plaintext
    plaintext = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d,
                 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
    key = "2b7e151628aed2a6"
    ciphertext = encrypt(plaintext, key)
    recovered = decrypt([row[:] for row in ciphertext], key)
    recovered_bytes = [recovered[r][c] for c in range(4) for r in range(4)]
    assert recovered_bytes == plaintext

    # Roundtrip test 2: readable plaintext
    plaintext2 = list("Hello, World!   ".encode('utf-8'))
    key2 = "supersecretkey"
    ciphertext2 = encrypt(plaintext2, key2)
    recovered2 = decrypt([row[:] for row in ciphertext2], key2)
    recovered_bytes2 = [recovered2[r][c] for c in range(4) for r in range(4)]
    assert recovered_bytes2 == plaintext2
    assert bytes(recovered_bytes2).decode('utf-8') == "Hello, World!   "

    # Roundtrip test 3: short key with padding
    plaintext3 = [0x00] * 16
    key3 = "secret"
    ciphertext3 = encrypt(plaintext3, key3)
    recovered3 = decrypt([row[:] for row in ciphertext3], key3)
    recovered_bytes3 = [recovered3[r][c] for c in range(4) for r in range(4)]
    assert recovered_bytes3 == plaintext3