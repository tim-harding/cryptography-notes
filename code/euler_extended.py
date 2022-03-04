from sys import argv

def main():
    try:
        main_inner()
    except Exception as e:
        print(e.args[0])
        return -1

def main_inner():
    if len(argv) != 3:
        raise Exception("Usage: python euler_extended.py [a] [b]")

    a = parse_arg(1)
    b = parse_arg(2)
    if b > a:
        tmp = a
        a = b
        b = tmp

    stages = calculate_stages(a, b)
    display_stages(stages)

    print(f"\nThe GCD is {stages[-2].r}")

def display_stages(stages):
    lines = []
    maximum_lengths = [0, 0, 0, 0, 0, 0]
    for stage in stages[2:]:
        parts = [
            f"{stage.a}",
            f"{stage.b}({stage.q})",
            f"{stage.r}",
            f"{stage.a}({stage.x})",
            f"{stage.b}({stage.y})",
            f"{stage.r}",
        ]
        for i, part in enumerate(parts):
            l = len(part)
            if l > maximum_lengths[i]:
                maximum_lengths[i] = l

        lines.append(parts)

    for line in lines:
        pad = []
        for i, part in enumerate(line):
            l = maximum_lengths[i]
            pad.append(part.ljust(l))
        print(f"{pad[0]} = {pad[1]} + {pad[2]}        {pad[3]} + {pad[4]} = {pad[5]}")

def calculate_stages(a, b):
    stages = [
        Stage(a, b, -1, -1, 1, 0),
        Stage(a, b, -1, -1, 0, 1),
    ]
    r = -1
    while r != 0:
        # a = b * q + r
        q = a // b
        r = a % b

        x, y = calculate_x_y(stages, q)

        stage = Stage(a, b, r, q, x, y)
        stages.append(stage)

        a = b
        b = r

    return stages

def calculate_x_y(stages, q):
    numerator = stages[-2]
    denominator = stages[-1]
    x = numerator.x - q * denominator.x
    y = numerator.y - q * denominator.y
    return (x, y)

class Stage:
    def __init__(self, a, b, r, q, x, y):
        self.a = a
        self.b = b
        self.r = r
        self.q = q
        self.x = x
        self.y = y

def parse_arg(i):
    n = 0
    arg = argv[i]
    try:
        n = int(arg)
    except Exception as e:
        raise Exception(f"Could not parse argument '{arg}' as an integer")

    if n <= 0:
        raise Exception(f"Expected '{n}' to be a natural number")

    return n

main()