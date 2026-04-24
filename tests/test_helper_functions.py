from aes.helperFunctions import *
"""
This file tests the helper functions in helperFunctions.py.
to run any of the test you must install run the command
python pip install pytest in the terminal. Then you can run the command
pytest test_helperFunctions.py to run all of the tests in this file.
"""
def test_getDegree():
    """ 
    Testing all of the cases for getDegree. This includes testing the degree of 0, 1, and 2 term polynomials as well as testing the degree of 0 which should return -1."""
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

def test_printStateBox(capsys):
    state = [
        [0xdb, 0x13, 0x53, 0x45],
        [0xf2, 0x0a, 0x22, 0x5c],
        [0x01, 0x01, 0x01, 0x01],
        [0xc6, 0xc6, 0xc6, 0xc6]
    ]

    printStateBox(state)

    captured = capsys.readouterr()

    assert "Current State Box:" in captured.out
    assert "db 13 53 45" in captured.out
    assert "f2 0a 22 5c" in captured.out
    