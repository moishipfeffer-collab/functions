def statistics(students):
    passed_students = 0
    sum = 0

    for student in students:
        passed_students += 1
        sum += student[1]

    average = sum / passed_students

    print("passed students:", passed_students)
    print("average:", average)