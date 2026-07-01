from grade_validation import gen_validate
from grade_logic import grade_cheking
from grade_output import statistics

def main():
    students = gen_validate()
    grade_cheking()
    statistics(students)

main()