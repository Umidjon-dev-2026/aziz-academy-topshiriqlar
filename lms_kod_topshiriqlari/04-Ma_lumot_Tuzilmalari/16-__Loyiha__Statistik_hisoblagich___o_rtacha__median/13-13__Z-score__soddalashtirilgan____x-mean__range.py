n = list(map(int, input().split()))
m, r = sum(n) / len(n), max(n) - min(n)
print(*(f"{(x - m) / r:.2f}" if r else "0.00" for x in n))