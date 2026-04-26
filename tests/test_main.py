from main import padKey, createStateBox
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
