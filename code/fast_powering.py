from sys import argv
import math

def main():
    if len(argv) != 4:
        print("Usage: python fast_powering.py [base] [exponent] [modulus]")
        return

    base = int(argv[-3])
    exponent = int(argv[-2])
    modulus = int(argv[-1])

    multiplier = base
    product = 1
    for i in range(int(math.ceil(math.log(exponent, 2)))):
        bit = (exponent >> i) & 1
        if bit == 1:
            product = (product * multiplier) % modulus

        print(f"{multiplier}^{{{bit}}} \\times ", end='')
        multiplier = (multiplier * multiplier) % modulus

    print(f"\n{base}^{{{exponent}}} \\equiv {product} \\pmod{{{modulus}}}")

main()
