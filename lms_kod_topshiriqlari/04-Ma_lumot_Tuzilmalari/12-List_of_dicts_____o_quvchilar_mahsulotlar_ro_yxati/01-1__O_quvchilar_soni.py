# N ta o‘quvchi beriladi
# Har biri: name score
# O‘quvchilar sonini chiqaring

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
print(len(students))