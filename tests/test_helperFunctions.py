from aes.helperFunctions import *
"""
This file tests the helper functions in helperFunctions.py.
to run any of the test you must install run the command
python pip install pytest in the terminal. Then you can run the command
python -m pytest -v 
"""
def test_getDegree():
    """ 
    Testing all of the cases for getDegree. This includes testing the degree of 0, 1, and 2 
    term polynomials as well as testing the degree of 0 which should return -1.
    """
    assert getDegree(0x01) == 0
    assert getDegree(0x02) == 1
    assert getDegree(0x15) == 4
    assert getDegree(0x80) == 7
    assert getDegree(0x00) == -1

def test_polyMod(): 
    """
    Testing some cases for polyMod
    this includes when a is less than m, and when a is 
    greater than.
    """
    assert polyMod(0x87, 0x11B) == 0x87
    assert polyMod(0x3A5, 0x11B) == 0x088
    assert polyMod(0x1F5, 0x11b) == 0x0EE   
    assert polyMod(0x00, 0x11B) == 0x00

def test_polyDivide():
    """
    Testing some cases for polyDivide
    """
    assert polyDivide(0x00, 0x11B) == 0x00  # zero case
    assert polyDivide(0x87, 0x11B) == 0x00  # degree < m, quotient is 0
    assert polyDivide(0x3A5, 0x11B) == 0x03  # two iterations

def test_polyMultiply():
    """
    Testing cases for poly multiply
    this include 0, 1 and when the result is greater than 0x11B and needs to be reduced.
    """
    assert polyMultiply(0x00, 0x83) == 0x00  # zero case
    assert polyMultiply(0x01, 0x57) == 0x57  # multiply by 1 stays same
    assert polyMultiply(0x02, 0x01) == 0x02  # simple case
    assert polyMultiply(0xFF, 0x02) == 0xE5 # testing reduction by irreducible polynomial

def printStateBox(state):
    """
    This prints the current AES state box as a 4x4 matrix.
    Each byte is printed in hexadecimal so it is easier to read
    during encryption and decryption.

    Args:
        state: a 4x4 array of byte values

    Returns:
        nothing, it only prints the state box
    """
    print("Current State Box:")

    for r in range(4):
        # Print each row cleanly with no trailing space
        print(" ".join(f"{state[r][c]:02x}" for c in range(4)))

def test_xGCD():
    """
    Testing cases for xGCD
    """
    gcd, s, t = xGCD(0x53, 0x11B)
    assert gcd == 0x01                        # irreducible poly always gives gcd of 1
    assert polyMultiply(0x53, s) == 0x01      # s is the inverse of 0x53
    assert s == 0xCA                          # AES known inverse of 0x53 is 0xCA

    gcd2, s2, t2 = xGCD(0x01, 0x11B)
    assert gcd2 == 0x01                       # gcd of 1 and irreducible poly is 1
    assert polyMultiply(0x01, s2) == 0x01     # inverse of 1 is 1

    gcd3, s3, t3 = xGCD(0x00, 0x11B)
    assert gcd3 == 0x11B                      # gcd of 0 and m is m
    
def test_printRoundKeys(capsys):
    round_keys = [
        [0x2b, 0x7e, 0x15, 0x16],
        [0x28, 0xae, 0xd2, 0xa6],
        [0xab, 0xf7, 0x15, 0x88],
        [0x09, 0xcf, 0x4f, 0x3c]
    ]

    printRoundKeys(round_keys)

    captured = capsys.readouterr()

    assert "Round Keys:" in captured.out
    assert "W0: 2b 7e 15 16" in captured.out
    assert "W1: 28 ae d2 a6" in captured.out
    assert "W2: ab f7 15 88" in captured.out
    assert "W3: 09 cf 4f 3c" in captured.out