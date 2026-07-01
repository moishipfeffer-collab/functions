from grad_data import get_students
from grade_validation import gen_validate
def main():
    students=get_students()
    validation=gen_validate()
    passed_students=0
    avrage=0
    sum=0
    for student in students:
        if len(student)==2:
            if type(student[1])==int:
                if 0< student[1] <100:
                    if type(student[0])==str:
                        if type(student)==tuple:
                            if 100> student[1]>=90:
                                print(student[0], student[1], "Excellent")
                            elif 60<= student[1] <=89:
                                print(student[0], student[1], "passed")
                            elif 0< student[1] <60:
                                print(student[0],student[1], "failed")
                            passed_students+=1
                            sum+=student[1]      
                        else:
                            print("Data must be a tuple")        
                    else:
                        print("Name must be a string")
                else:
                    print("Grade must be between 0 and 100")
            else:
                print("Grade must be an integer")
        else:
            print("the tuple contains more then 2")
    avrage=sum/passed_students        
    print("passed students:", passed_students)
    print("avrage:", avrage)
main()