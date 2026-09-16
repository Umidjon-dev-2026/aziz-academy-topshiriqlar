# N ta o‘quvchi
# Eng katta bahoga ega o‘quvchi nomini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
best_student = max(students, key=lambda x: x['score'])
print(best_student['name'])