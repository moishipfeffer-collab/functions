def get_number_sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    elif number == 0:
        return "Zero"
def get_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def count_above_average(numbers):
    count=0
    for number in numbers:
        if number > calculate_average(numbers):
            count+=1
        return count

