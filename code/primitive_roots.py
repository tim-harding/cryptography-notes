def problem_e():
    p = 229
    count = 0
    for g in range(2, p):
        power = g
        is_primitive_root = True
        for i in range(0, p - 2):
            if power == 1:
                is_primitive_root = False
                break
            power = (power * g) % p
        if is_primitive_root:
            print(g)
            count += 1
    print(count)


def problem_f():
    primes_under_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
    ]
    for p in primes_under_100:
        power = 2
        has_primitive_root_2 = True
        for i in range(0, p - 2):
            if power == 1:
                has_primitive_root_2 = False
                break
            power = (power * 2) % p
        if has_primitive_root_2:
            print(p)


problem_f()
