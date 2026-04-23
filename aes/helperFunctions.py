## Holding all of the helper functions for AES shared between groups

# We need 

## Calculate Degree of Poly
def getDegree(a):
    for i in range(7, -1, -1):
        if (a >> i) & 1:
            return i
    return -1
## Calculate Modular Inverse over arbitrary m(x)

## Calculate Polynomial Multiplication over arbitrary m(x)

## Print Current State Box

## Print Round Keys (W0 to W43 MUST BE HEXADECIMAL)

## Print Plaintext > Cyphertext > RecoverText
