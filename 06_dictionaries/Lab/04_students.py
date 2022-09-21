courses = {}
students = {}
course = ''
while True:
    st = input()
    if st.replace('_', ' ') in courses:
        course = st.replace('_', ' ')
        break
    st = st.split(':')
    student = st[0]
    student_id = int(st[1])
    course = st[2]
    if course not in courses:
        courses[course] = [student]
        students[student] = student_id
    else:
        courses[course] += [student]
        students[student] = student_id
for student in students:
    if student in courses[course]:
        print(f'{student} - {students[student]}')
