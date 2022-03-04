from sys import argv

def main():
    if len(argv) != 3:
        print("Expected two arguments")
        return

    a = int(argv[1])
    if a is None:
        print(f"Could not parse argument {argv[1]} as a number")
        return

    b = int(argv[2])
    if b is None:
        print(f"Could not parse argument {argv[2]} as a number")
        return

    while b != 0:
        r = a % b
        a = b
        b = r

    print(a)

main()
