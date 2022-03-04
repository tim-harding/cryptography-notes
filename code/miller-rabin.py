import random
from sys import argv
from tokenize import maybe

def main():
    if len(argv) != 2:
        print("Usage: python miller-rabin.py [n]")
        return -1

    n = int(argv[-1])
    print(is_probably_prime(n, 10))

def is_probably_prime(n, rounds):
    k = 0
    q = n - 1
    while q % 2 == 0:
        k += 1
        q //= 2

    print(f"k &= {k} \\\\")
    print(f"q &= {q} \\\\")
    print("\\\\")

    maybe_prime = True
    for _ in range(rounds):
        a = random.randrange(2, n)
        maybe_prime &= not is_definitely_composite(n, a, k, q)
        print("\\\\")

    return maybe_prime

def is_definitely_composite(n, a, k, q):
    a0 = a

    if n % 2 == 0:
        return True

    for _ in range(1, q):
        a = (a * a0) % n

    if a == 1:
        return False

    for i in range(0, k):
        print(f"{a0}^{{2^{{{i}}} {q}}} &\\equiv {a} \\pmod{{{n}}} \\\\")
        if a == n - 1:
            return False
        a = (a * a) % n

    return True

main()