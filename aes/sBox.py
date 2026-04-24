from aes.helperFunctions import * 
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
    return s & 0xFF

def rotate(b, n):
    """
    This function just a small shortcut for readability
    it does the circular rotation for the bits up to 8
    """
    return ((b << n) | (b >> (8 - n))) & 0xFF # This shifts the bits circular but keeps it below 8 bits 

## Next on list is to create the 2D array that holds all of that subbytes :(
def generateSBox ():
    """
    This is generating the sBox for in a 16x16 array
    """
    sBox = [[0] * 16 for _ in range (16)] # Creates a 2D array that we fill in
    for i in range(0, 256):
        sBox[i//16][i%16] = subByte(i)
    return sBox
def printSBox(sBox):
    for row in sBox:
        for val in row:
            print(f"{val:02x}", end=" ")
        print()

def generateInvSBox():
    sBox = generateSBox()
    invSBox = [[0] * 16 for _ in range (16)] # Creates a 2D array that we fill in

    for i in range (256):
        currentValue = sBox[i//16][i%16] 
        invSBox[currentValue //16][currentValue%16] = i # this line takes the current value were in 
        # and then determines the row and column then places it in its spot respectively for example index 0x00 has value 63 it put 00 in row 6 col 3
    return invSBox
