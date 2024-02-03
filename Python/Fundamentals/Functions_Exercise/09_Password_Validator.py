import string


def it_is_long_enough(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        return False


def it_is_only_from_letters_and_digits(password):
    letters = string.ascii_letters
    digits = string.digits
    for char in password:
        if not (char in letters or char in digits):
            return False
    return True


def is_there_enough_digits(password):
    digits = string.digits
    digits_count = 0
    for char in password:
        if char in digits:
            digits_count += 1
            if digits_count == 2:
                return True
    return False


def password_is_valid(password):
    if is_there_enough_digits(password) and it_is_long_enough(password) and it_is_only_from_letters_and_digits(
            password):
        return "Password is valid"
    messages = []
    if not it_is_long_enough(password):
        messages.append("Password must be between 6 and 10 characters")
    if not it_is_only_from_letters_and_digits(password):
        messages.append("Password must consist only of letters and digits")
    if not is_there_enough_digits(password):
        messages.append("Password must have at least 2 digits")
    return "\n".join(messages)


print(password_is_valid(input()))
