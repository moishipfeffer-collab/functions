from grade_validation import gen_validate
def grade_cheking():
    students=gen_validate()    
    for student in students:
                            if 100> student[1]>=90:
                                print(student[0], student[1], "Excellent")
                            elif 60<= student[1] <=89:
                                print(student[0], student[1], "passed")
                            elif 0< student[1] <60:
                                print(student[0],student[1], "failed")
