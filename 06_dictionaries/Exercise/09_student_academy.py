lines = int(input())
students = {}
students_left = {}

while lines:
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = [grade]
    else:
        students[student].append(grade)
    lines -= 1

for student, grades in students.items():
    avg = sum(grades) / len(grades)
    if avg >= 4.5:
        students_left[student] = avg

for student, grade in students_left.items():
    print(f'{student} -> {grade:.2f}')