n = int(input())
students = []
for i in range(n):
    parts = input().split()
    students.append({"ism": parts[0], "baho": int(parts[1])})
total = 0
for s in students:
    total += s["baho"]
avg = total / n
for s in students:
    if s["baho"] > avg:
        print(s["ism"])