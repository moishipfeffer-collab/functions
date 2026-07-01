from grad_data import get_students
def val_name(name):
    if type(name)==str:
        return True


def val_grade(grade):
    if type(grade) != str and 0<= grade <=100:
        return True
        

def gen_validate ():
    students=get_students()
    for student in students:
        val_name(student[0])
        val_grade(student[1])


        
