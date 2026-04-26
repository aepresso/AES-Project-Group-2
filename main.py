import sys
from aes.sBox import generateSBox, generateInvSBox
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

    

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <key> <input_file> <output_file>")
        return
    
    key = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]
