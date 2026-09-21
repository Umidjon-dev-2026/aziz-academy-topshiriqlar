n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
best_point = max(points, key=lambda p: (p[0], -p[1]))
print(best_point[0], best_point[1])