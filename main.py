import sys
from aes.sBox import *
from aes.mixColumns import *
# from aes.keyExpansion import *  # stub until teammate finishes

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <key> <input_file> <output_file>")
        return
    
    key = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]