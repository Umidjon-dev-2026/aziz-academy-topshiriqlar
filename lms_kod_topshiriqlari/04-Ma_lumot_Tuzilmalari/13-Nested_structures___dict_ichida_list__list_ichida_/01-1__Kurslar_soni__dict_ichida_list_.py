# INPUT:
# 1-qator: n (kurslar soni)
# Keyingi n qator: course_name k student1 student2 ... studentk
# Vazifa: jami kurslar sonini chiqaring (n)

n = int(input().strip())
courses = []
for _ in range(n):
    parts = input().split()
    name = parts[0]
    k = int(parts[1])
    students = parts[2:2+k]
    courses.append({"name": name, "students": students})
print(len(courses))