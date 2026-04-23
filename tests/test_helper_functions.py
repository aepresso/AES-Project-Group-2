from aes.helperFunctions import getDegree

def test_getDegree():
    assert getDegree(0x01) == 0
    assert getDegree(0x02) == 1
    assert getDegree(0x15) == 4
    assert getDegree(0x80) == 7
    assert getDegree(0x00) == -1
