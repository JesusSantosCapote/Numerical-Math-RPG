import random


def generate_arithmetic():
    precision = random.randint(2, 9)
    exponent_digits = random.randint(1, 2)

    if exponent_digits == 1:
        min_exp = 0

    else:
        min_exp = "-"
        for i in range(exponent_digits - 1):
            min_exp = min_exp + "9"
        min_exp = int(min_exp)

    max_exp = ""
    for i in range(exponent_digits):
        max_exp = max_exp + "9"

    max_exp = int(max_exp)

    return (10, precision, min_exp, max_exp)

print(generate_arithmetic())    