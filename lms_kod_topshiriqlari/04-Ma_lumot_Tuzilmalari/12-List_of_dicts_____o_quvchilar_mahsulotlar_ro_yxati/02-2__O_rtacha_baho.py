# N ta o‘quvchi: name score
# O‘rtacha bahoni chiqaring (float)

n = int(input())
students = []
for _ in range(n):
    name, score = input().split()
    students.append({'name': name, 'score': int(score)})
# TODO
print(sum(s['score'] for s in students) / n)