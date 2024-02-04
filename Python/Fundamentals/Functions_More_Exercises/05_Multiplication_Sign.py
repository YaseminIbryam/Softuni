def is_zero(num):
    return num == 0


def is_positive(num):
    return num > 0


def multiplication_sign(num_1, num_2, num_3):
    if is_zero(num_1) or is_zero(num_2) or is_zero(num_3):
        return "zero"
    elif is_positive(num_1):
        if is_positive(num_2):
            if is_positive(num_3):
                return "positive"
            else:
                return "negative"
        else:
            if is_positive(num_3):
                return "negative"
            else:
                return "positive"
    else:
        if is_positive(num_2):
            if is_positive(num_3):
                return "negative"
            else:
                return "positive"
        else:
            if is_positive(num_3):
                return "positive"
            else:
                return "negative"


print(multiplication_sign(int(input()), int(input()), int(input())))
