from sys import argv

def main():
    if len(argv) != 4:
        print("Usage: python discrete_logarithm.py [base] [argument] [modulus]")
        return

    base = int(argv[-3])
    argument = int(argv[-2])
    modulus = int(argv[-1])

    current = 1
    for i in range(0, modulus):
        if current == argument:
            print(i)
            return
        current = (current * base) % modulus

    print("Could not compute")

main()