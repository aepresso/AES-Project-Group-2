## This will hold the code for Key Expansion and assigned to Malachi ##
import copy
from aes.sBox import *
"""
    Takes in the key as a hex byte array and the round count also as a hex byte. 
    Then performs the key expansion algorithm using 2 copies of the original key and returns the resulting key. 

    args: 
        initialKey: 4x4 matrix of hex byte values
        round_count: integer that indicates the round count
    
    returns: 
        resultKey: the resulting key from the key expansion in the same form as the original key.
"""
def keyExpansion(initialKey, round_count):
    rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    resultKey = copy.deepcopy(initialKey)
    tempKey = copy.deepcopy(initialKey)
    tempKey[3].append(tempKey[3].pop(0))
    for i in range(len(resultKey)):
        if i%4 != 0:
            for j in range(len(resultKey[i])):
                resultKey[i][j] = resultKey[i-1][j] ^ initialKey[i][j]
        else:
            resultKey[i] = tempKey[3]
            for j in range(len(resultKey[i])):
                resultKey[i][j] = subByte(resultKey[i][j])
            resultKey[i][0] ^= rcon[round_count-1]
            for j in range(len(resultKey[i])):
                resultKey[i][j] ^= initialKey[i][j]
    return resultKey
