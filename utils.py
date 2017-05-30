
import random

class BinaryConversionException(Exception):
    """Custom exception for invalid binary conversions"""
    pass

def is_superincreasing(seq):
    """Returns True iff `seq` is a superincreasing sequence"""
    ct = 0  # Total so far
    for n in seq:
        if n <= ct:
            return False
        ct += n
    return True


def modinv(a, b):
    """Returns the modular inverse of a mod b.

    Pre: a < b and gcd(a, b) = 1

    Adapted from https://en.wikibooks.org/wiki/Algorithm_Implementation/
    Mathematics/Extended_Euclidean_algorithm#Python
    """
    saved = b
    x, y, u, v = 0, 1, 1, 0
    while a:
        q, r = b // a, b % a
        m, n = x - u*q, y - v*q
        b, a, x, y, u, v = a, r, u, v, m, n
    return x % saved


def coprime(a, b):
    """Returns True iff `gcd(a, b) == 1`, i.e. iff `a` and `b` are coprime"""
    while b:
        a, b = b, a % b
    return a == 1


def byte_to_bits(byte):
    if not 0 <= byte <= 255:
        raise BinaryConversionException()

    out = []
    for i in range(8):
        out.append(byte & 1)
        byte >>= 1
    return out[::-1]


def bits_to_byte(bits):
    if not all(bit == 0 or bit == 1 for bit in bits):
        raise BinaryConversionException("Invalid bitstring passed")

    byte = 0
    for bit in bits:
        byte *= 2
        if bit:
            byte += 1
    return byte




