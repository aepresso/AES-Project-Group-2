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

    This functions used to help make mod inverse and polynomial multiplication easier to implement.
    """
    if (getDegree(a) == -1 or getDegree(m) == -1):
        return 0
    while getDegree(a) >= getDegree(m):
        a ^= m << (getDegree(a) - getDegree(m))
    return a

def polyDivide(a, b):
    """ 
    This calculates the polynomial division of a by b. 
    Super similar to polyMod but im returning the quotient instead of the remainder.
    
    args: a and b are polynomials as integers
    returns the quotient of a divided by b as an integer
    """
    if (getDegree(a) == -1 or getDegree(b) == -1):
        return 0
    quotient = 0
    while getDegree(a) >= getDegree(b):
        quotient |= 1 << (getDegree(a) - getDegree(b))
        a ^= b << (getDegree(a) - getDegree(b))
    return quotient

def polyMultiply(a,b):
    """
    This calculates the polynomials multiplication of a and b.
    args: a and b are polynomials as integers
    returns the product of a and b as an integer
    """
    if (getDegree(a) == -1 or getDegree(b) == -1): 
        return 0
    result = 0
    for i in range (16):
        if (b >> i) & 1:
            result ^= a << i
    return polyMod(result, 0x11B) # Modulo by the irreducible polynomial for AES

def xGCD(a,m):
    """
    This uses extended Euclidean to calculate GCD of a and m
    args: a and m are polynomials as integers
    returns the GCD of a and m as an integer and s and t such that a*s + m*t = GCD(a,m)
    """
    if (getDegree(m) == -1):
        return a, 1, 0
    
    q = polyDivide(a, m)
    r = polyMod(a, m)
    gcd, s1, t1 = xGCD(m, r) # Using recursion to calculate the GCD of m and r, which is the remainder of a divided by m

    s = t1
    t = s1 ^ polyMultiply(q, t1)

    return gcd, s, t
    



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
def printStateBox(state):
    """
    This prints the current AES state box as a 4x4 matrix.
    Each byte is printed in hexadecimal so it is easier to read
    during encryption and decryption.
    """
    print("Current State Box:")

    for r in range(4):
        for c in range(4):
            # print each byte as two hexadecimal digits
            print(f"{state[r][c]:02x}", end=" ")
        print()
## Print Round Keys (W0 to W43 MUST BE HEXADECIMAL)

## Print Plaintext > Cyphertext > RecoverText
