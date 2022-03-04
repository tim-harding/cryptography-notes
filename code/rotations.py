from sys import argv

def main():
    text = argv[-1]
    for i in range(26):
        str = ""
        for character in text:
            c = ord(character) - ord('A')
            c = (c + i) % 26
            str += chr(c + ord('A'))
        print(str)

main()
