n = int(input())
items = []
for _ in range(n):
    name, qty, price = input().split()
    qty, price = int(qty), int(price)
    items.append((name, qty, price, qty * price))
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

for name, qty, price, total in items:
    print(f"{name:<12} | {qty:>5} | {price:>7} | {total:>9}")
     
best = max(items, key=lambda x: (x[3], [-ord(c) for c in x[0]]))
print(f"BEST: {best[0]} {best[3]}")