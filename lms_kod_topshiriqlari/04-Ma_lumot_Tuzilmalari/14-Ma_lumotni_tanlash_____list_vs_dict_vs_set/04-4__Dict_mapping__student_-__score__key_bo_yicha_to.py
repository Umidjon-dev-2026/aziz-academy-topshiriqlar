n = int(input())
scores = {}
for _ in range(n):
    name, score = input().split()
    scores[name] = score 
q = int(input())
for _ in range(q):
    name = input()
    if name in scores:
        print(scores[name])
    else:
        print("NOT_FOUND")