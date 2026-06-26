n = int(input())
for i in range(n):
    print("".join("*" if i == j or i + j == n - 1 else "." for j in range(n)))