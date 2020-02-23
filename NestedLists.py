from operator import itemgetter
students = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student = [name, score]
    students.append(student)
    students.sort(key=itemgetter(0))
    students.sort(key=itemgetter(1))

a = students.pop(0)
for i in range(len(students)):
    if (students[0][1]==a[1]):
        students.pop(0)
print(students[0][0])
for i in range(len(students)-1):
    if(students[i+1][1] == students[0][1]):
        print(students[i+1][0])
    else:
        break

