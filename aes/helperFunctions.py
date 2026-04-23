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

## Print Current State Box

## Print Round Keys (W0 to W43 MUST BE HEXADECIMAL)

## Print Plaintext > Cyphertext > RecoverText
