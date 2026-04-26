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
    
    # flatten initialKey into list of 4 words W[0]-W[3]
    W = [[initialKey[j][i] for j in range(4)] for i in range (4)]
    
    # generate W[4] through W[4*round_count+3]
    for i in range(4, 4 * round_count + 4):
        temp = W[i-1][:]
        if i % 4 == 0:
            temp.append(temp.pop(0))  # RotWord
            temp = [subByte(b) for b in temp]  # SubWord
            temp[0] ^= rcon[(i // 4) - 1]  # XOR Rcon
        W.append([W[i-4][j] ^ temp[j] for j in range(4)])
    
    # return the round_count-th round key as 4x4 matrix
    start = 4 * round_count
    round_words = [W[start + i] for i in range(4)]
    return [[round_words[col][row] for col in range(4)] for row in range(4)]