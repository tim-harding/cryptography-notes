def main():
    pairs = [
        (34787, 353),
        (238792, 7843),
        (9829387493, 873485),
        (1498387487, 76348),
        (78745, 127),
        (2837647, 4387),
        (8739287463, 18754),
        (4536782793, 9784537),
    ]

    for pair in pairs:
        a, b = pair
        frac = a / b
        q = a // b
        r = a % b

        print("\\begin{align*}")
        print(f"    \\frac{{{a}}}{{{b}}} =& {frac} \\\\")
        print(f"    q =& {q} \\\\")
        print(f"    r =& {frac - q} \\times {b} \\approx {r}")
        print("\\end{align*}\n")

main()