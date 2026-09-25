n = int(input())
student = []
for _ in range(n):
    name, score = input().split()
    student.append((name, int(score)))
student.sort(key=lambda x: (-x[1], x[0]))
print(f"{'Name':<10} | {'Score':>5}")
print("-" * 10 + "+" + "-" * 5)

for name, score in student:
    print(f"{name:<10} | {score:>5}")