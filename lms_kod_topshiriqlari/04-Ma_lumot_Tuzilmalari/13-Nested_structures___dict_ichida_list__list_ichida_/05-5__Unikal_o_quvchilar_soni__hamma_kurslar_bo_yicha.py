# INPUT:
# n
# n qator: course_name k student1 ... studentk
# Vazifa: hamma kurslar bo‘yicha unikal o‘quvchilar sonini chiqaring.
# (Bir o‘quvchi bir nechta kursda bo‘lishi mumkin.)

n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({'name': name, 'students': students})

# TODO
unikal = set()
for c in courses:
    for s in c['students']:
        unikal.add(s)
print(len(unikal))