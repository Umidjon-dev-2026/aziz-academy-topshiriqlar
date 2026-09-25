n = int(input())
items = []
grand_total = 0
for _ in range(n):
    name, qty, price = input().split()
    qty, price = int(qty), int(price)
    total = qty * price
    grand_total += total
    items.append((name, qty, price, total))
print(f"{'Product':<12} | {'Qty':>5} | {'Price':>7} | {'Total':>9}")
print("-" * 12 + "+" + "-" * 5 + "+" + "-" * 7 + "+" + "-" * 9)

for name, qty, price, total in items:
    print(f"{name:<12} | {qty:>5} | {price:>7} | {total:>9}")
print(f"GRAND: {grand_total}")