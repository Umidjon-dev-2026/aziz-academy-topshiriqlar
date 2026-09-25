n = int(input())
student = []
for _ in range(n):
    name, score = input().split()
    student.append((name, int(score)))
x = int(input())
tanlangan = []

for name, score in student:
    if score >= x:
        tanlangan.append((name, score))
if tanlangan:
    for name, score in tanlangan:
        print("{}={}".format(name, score))
else:
    print("EMPTY")