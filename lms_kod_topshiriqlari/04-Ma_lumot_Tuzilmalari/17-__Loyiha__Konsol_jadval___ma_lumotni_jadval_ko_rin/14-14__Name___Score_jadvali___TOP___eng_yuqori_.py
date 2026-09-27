n = int(input())
student = []
for _ in range(n):
    name, score = input().split()
    score = int(score)
    student.append((name, score))

print(f"{'Name':<10} | {'Score':>5}")
print("----------+-----")
for name, score in student:
    print(f"{name:<10} | {score:>5}")
best_name, best_score = min(student, key=lambda x: (-x[1], x[0]))
print(f"TOP: {best_name} {best_score}")