from main import padKey
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

    
