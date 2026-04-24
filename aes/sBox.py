from helperFunctions import * 
"""
This file is the subBox file that converts or substitutes those bytes needed
for the AES encryption

"""
def subByte(a): 
    """
    This take in a byte  
    it doesnt use the actual graph but rather
    what the box lookup table represents
    args: a the byte 
    returns: s the substituted byte. 
    """
    b = modInverse(a, 0x11B) # b will hold the mod inverse value needed for later
    s = b ^ rotate(b, 1) ^ rotate(b,2) ^ rotate(b,3) ^ rotate(b,4) ^ 0x63
    #  The line above xors the mod inverse by itself but at different circular rotations
    #  Then finally it xored with 0x63 which is the constant.
    return s ^ 0xFF

def rotate(b, n):
    """
    This function just a small shortcut for readability
    it does the circular rotation for the bits up to 8
    """
    return ((b << n) | (b >> (8 - n))) & 0xFF # This shifts the bits circular but keeps it below 8 bits 


