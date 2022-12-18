import random
import math
from numpy import format_float_scientific


def generate_arithmetic():
    """
    Generate a random floating point arithmetic with base 10
    """

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


def get_representation(number, arithmetic):
    """
    Returns a tuple that in the first position has the representation of 
    'number' in the arithmetic 'arithmetic' by truncation and in the 
    second by rounding to the nearest float.
    """

    arithmetic_min = arithmetic[0]**(arithmetic[2]-1)
    arithmetic_max = "."

    for i in range(arithmetic[1]):
        arithmetic_max = arithmetic_max + "9"

    arithmetic_max = arithmetic_max + "e" + str(arithmetic[3])
    arithmetic_max = float(arithmetic_max)

    if number > arithmetic_max: return ("inf", "inf")
    
    elif number < arithmetic_min: return ("0", "0")

    else:
        number = float(number).__str__()
        comma_pos = number.index('.')
        first_digit_pos = 0
        for i in range(len(number)):
            if number[i] != "0" and number[i] != ".":
                first_digit_pos = i
                break

        if first_digit_pos < comma_pos:
            exp = abs(first_digit_pos - comma_pos)

        else: exp = comma_pos - first_digit_pos  + 1

        trunc = ["0" for i in range(arithmetic[1])]
        closest = ["0" for i in range(arithmetic[1])]
        aux_number = [number[i] for i in range(first_digit_pos, len(number)) if number[i] != "."]
        precision_copy = arithmetic[1]

        for i in range(min(arithmetic[1], len(aux_number))):
            trunc[i] = aux_number[i]
            closest[i] = aux_number[i]

        if arithmetic[1] < len(aux_number):
            digit = int(aux_number[arithmetic[1]])
            if digit >= 5:
                last_digit = closest[len(closest)-1]
                last_digit = int(last_digit) + 1
                last_digit = str(last_digit)
                closest[len(closest)-1] = last_digit

        trunc.append("E")
        closest.append("E")
        exp = str(exp)
        trunc.append(exp)
        closest.append(exp)

        trunc_result = "."
        closest_result = "."

        for item in trunc:
            trunc_result = trunc_result + item

        for item in closest:
            closest_result = closest_result + item

        return (trunc_result, closest_result)

print(get_representation(0.0032, (10, 3, -9, 99)))
