MAX = 300

def main():
    odds_from_three = [True for i in range(MAX)]
    for i, is_prime in enumerate(odds_from_three):
        if is_prime:
            n = index_to_number(i)
            for mask in range(2 * n, MAX, n):
                odds_from_three[mask] = False

    print(2)
    for i, is_prime in enumerate(odds_from_three):
        if is_prime:
            print(index_to_number(i))

def index_to_number(i):
    return 3 + 2 * i

main()
