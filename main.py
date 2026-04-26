import sys
from aes.sBox import generateSBox, generateInvSBox, subByte
from aes.mixColumns import mixColumns, invMixColumns, shiftRows, invShiftRows
from aes.keyExpansion import keyExpansion  

def createStateBox(blockOfBytes):
    """
    This takes in the bytes in an
    array and then organizes it in a 2D array
    in state box column fashion
    args: blockOfBytes, an array filled with 16 bytes 
    returns: a 2D array that organized the block argument into state box
    """
    stateBox = [[0]* 4 for _ in range (4) ] # creates a 2D array that gets filled in
    for i in range (16):
        stateBox [i%4][i//4] = blockOfBytes[i]
    return stateBox

def addRoundKey(stateBlock, roundKeyBlock):
    """
    Takes in the stateBlock bytes
    and then xors the round key to each 
    byte in the state block

    args: stateBlock and roundKeyBlock; both 2D arrays
    returns: stateBlock, this is after adding that round key.
    """
    for row in range (4):
        for col in range (4):
            stateBlock[row][col] ^= roundKeyBlock[row][col]
    return stateBlock

def subBytes(stateBox):
    """
    This applies subByte to the entire state box
    giving the substitution needed.
    does this by applying the subByte functions to every byte in the state
    by iterating through it in a 2D array

    args: stateBox, a 2D array that holds the current state
    returns: subState, the stateBox after subByte was applied all bytes in it
    """
    for row in range (4):
        for col in range (4):
            stateBox[row][col] = subByte(stateBox[row][col]) # this applies the function subByte to every byte in the state
    return stateBox

def invSubBytes(stateBox):
    """
    This function is use for decryption where we take the e
    cipher text and turn it back into it output text
    
    args: stateBox, a 2D array of bytes
    returns: invSubBytes of the array
    """
    invSBox = generateInvSBox()
    for row in range (4):
        for col in range (4):
            b = stateBox[row][col]
            stateBox[row][col] = invSBox[b >> 4][b & 0x0F]
    return stateBox


def padKey(key):
    """
    This will parse a string from the user input 
    and pad or trim depending on what is needed so we can use it as a key
    args: key, a string
    returns: padded or trimmed key in form of byte
    """
    if not isinstance (key, str):
        raise TypeError("Key must be a string") # wrong type error
    
    while len(key) < 16:
        key = key + " "

    if len(key) > 16:
        key = key[:16]
    return key.encode('utf-8')

def generateAllRoundKeys(initialKey):
    roundKeys = [initialKey]
    for i in range(1, 11):
        nextKey = keyExpansion(initialKey, i)
        roundKeys.append(nextKey)
    return roundKeys

def encrypt(plaintext, key):
    """
    Getting to the meat of the aes 
    is this encrpyt function
    it'll used createStateBox, padKey, addRoundKey and almost all functinons
    
    args: plaintext as 16 bytes, and key as a string
    returns the state box after encryption
    """ 
    paddedKey = padKey(key) # applying padkey to the key
    paddedKey = createStateBox(paddedKey) # converting to 2D array for usage in key expansion
    roundKeys = generateAllRoundKeys(paddedKey) # this line generates a round key for 11 rounds
    
    theState = createStateBox(plaintext)
    
    addRoundKey(theState, roundKeys[0])
    
    for i in range (1,10):
        subBytes(theState)
        theState = shiftRows(theState)
        theState =mixColumns(theState)
        addRoundKey(theState, roundKeys[i])

    subBytes(theState)
    theState = shiftRows(theState)
    addRoundKey(theState, roundKeys[10])
    
    return theState
    
def decrypt(ciphertext, key):
    paddedKey = padKey(key)
    paddedKey = createStateBox(paddedKey)
    roundKeys = generateAllRoundKeys(paddedKey)
    
    theState = ciphertext #state box is current cipher text but we unravel it
    
    #initial round key xor
    addRoundKey(theState, roundKeys[10])
    
    # rounds 9 - 1 reverse order inverse operations
    for i in range (9,0,-1):
        theState = invShiftRows(theState)
        theState = invSubBytes(theState)
        addRoundKey(theState, roundKeys[i])
        theState = invMixColumns(theState)
        
    theState = invShiftRows(theState)
    theState = invSubBytes(theState)
    addRoundKey(theState,roundKeys[0])
    
    return theState
    
def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <key> <input_file> <output_file>")
        return
    
    key = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

