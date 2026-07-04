def validate_number(number):
    if type(number) != int:
        raise TypeError("number must be an integer")
