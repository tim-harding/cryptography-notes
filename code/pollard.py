def main():
    print(gcd(25, 35))  # 5
    print(gcd(14, 70))  # 7
    print("\n")
    print("\n")
    print_pollard(35, 2)
    print_pollard(1739, 2)
    print_pollard(220459, 2)
    print_pollard(48356747, 2)


def print_pollard(N, a):
    p = pollard(N, a)
    print(f"{N} = {p} * {N // p}\n")


def gcd(a, b, m=1):
    remainder = a % b
    if remainder == 0:
        return m
    else:
        return gcd(b, remainder, remainder)


def pollard(N, a, n=1):

    next_a = 1
    # n is the factorial iteration we're on,
    # N is the number we're trying to factor.
    # a is the base we're trying to use.
    for _ in range(n):
        next_a = (next_a * a) % N
    b = (next_a - 1) % N
    m = gcd(b, N)
    print(f"{a}^{{{n}}} - 1 &\\equiv {b} \\pmod{{{N}}} & \\gcd({b}, {N}) &= {m} \\\\")
    if m == 1:
        return pollard(N, next_a, n + 1)
    elif m == N:
        return -1
    else:
        return m


main()
