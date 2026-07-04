from number_data import get_numbers
from number_validation import validate_number
from number_logic import get_number_sign,get_even_odd,calculate_average,count_above_average
from number_output import print_number_result,print_skipped_number,print_number_summary
def run_number_analyzer():
    numbers=get_numbers()
    valid_numbers=[]
    for number in numbers:
        try:
            validate_number(number)
            sign=get_number_sign(number)
            even_odd=get_even_odd(number)
            print_number_result(number,sign,even_odd)
            valid_numbers.append(number)

        except TypeError as error:
            print_skipped_number(error)
    average=calculate_average(valid_numbers)
    count=count_above_average(valid_numbers)
    print_number_summary(average,count)

        