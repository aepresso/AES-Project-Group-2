import sys
from aes.sBox import generateSBox, generateInvSBox
from aes.mixColumns import mixColumns, invMixColumns, shiftRows, invShiftRows
# from aes.keyExpansion import *  # stub until teammate finishes
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
