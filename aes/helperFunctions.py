## Holding all of the helper functions for AES shared between groups

def getDegree(a):
    """
    This gets the degree of any polynomial represented as an integer. 
    an example is 0x15 which is 0001 0101 in binary which 
    can be written as x^4 + x^2 + 1; this has a degree of 4.
    
    Args: the polynomial such as 0x01 or 0001 
    Returns: the degree of the polynomial, -1 if the polynomial is 0
    """
    for i in range(15, -1, -1):
        if (a >> i) & 1:
            return i
    return -1

## Calculating polynomial modulo 
def polyMod(a, m):
    """
    This calculates the polynomial modulo of a by m. 
    a gets divided by m and the remainder is returned.
    
    args: a and m are polynomials as integers
    returns the remainder of a divided by m as an integer
    """
    if (getDegree(a) == -1 or getDegree(m) == -1):
        return 0
    while getDegree(a) >= getDegree(m):
        a ^= m << (getDegree(a) - getDegree(m))
    return a
## Calculate Modular Inverse over arbitrary m(x)

## Calculate Polynomial Multiplication over arbitrary m(x)
def gfMultiply(a, b):
    """
    This multiplies two bytes in the AES Galois Field GF(2^8).
    AES uses the irreducible polynomial 0x11B when reducing values
    that go over 8 bits.

    Args:
        a: first byte value
        b: second byte value

    Returns:
        the multiplied byte value reduced to 8 bits
    """
    result = 0

    for i in range(8):
        # If the lowest bit of b is 1, add a to the result using XOR
        if b & 1:
            result ^= a

        # Check if a will overflow past 8 bits
        carry = a & 0x80

        # Multiply a by x, which is the same as shifting left
        a <<= 1

        # If it overflowed, reduce it using AES polynomial 0x11B
        if carry:
            a ^= 0x11B

        # Keep only the lowest 8 bits
        a &= 0xFF

        # Move to the next bit of b
        b >>= 1

    return result

## Print Current State Box

## Print Round Keys (W0 to W43 MUST BE HEXADECIMAL)

## Print Plaintext > Cyphertext > RecoverText
