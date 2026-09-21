# INPUT:
# 1-qator: n
# keyingi n qator: name score
# VAZIFA:
# - har o‘quvchini dict ko‘rinishida saqlang: {'name':..., 'score':...}
# - eng katta score toping
# - agar teng bo‘lsa name kichigi yutsin
# OUTPUT: name score
n = int(input())
students = []
for i in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
best_student = min(students, key=lambda s: (-s['score'], s['name']))    
print(f"{best_student['name']} {best_student['score']}")