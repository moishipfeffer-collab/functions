from grad_data import get_students
def val_name(name):
    if type(name)==str:
        return True


def val_grade1(grade):
    if type(grade) == str:
        return True
def val_grade2(grade):
    if grade >100 or grade <0:
        return True
        

def gen_validate():
    students = get_students()
    valid_students = []

    for student in students:
        if type(student) != tuple:
            print("Data must be a tuple")
            continue

        if len(student) != 2:
            continue

        if not val_name(student[0]):
            print("Name must be a string")
            continue

        if val_grade1(student[1]):
            print("Grade must be an integer")
            continue
        if val_grade2(student[1]):
            print("Grade must be between 0 and 100")
            continue

        valid_students.append(student)

    return valid_students