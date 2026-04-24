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
    