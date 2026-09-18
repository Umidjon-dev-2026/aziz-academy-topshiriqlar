# INPUT:
# n
# n qator: category name price qty
# Vazifa: har category bo‘yicha total sum = Σ(price*qty)
# Output: categorylar alifbo bo‘yicha sort bo‘lsin
# Har qator: category total

n = int(input().strip())
items = []
for _ in range(n):
    cat, name, price, qty = input().split()
    items.append({'cat': cat, 'name': name, 'price': int(price), 'qty': int(qty)})

# TODO
c_t = {}
for item in items:
    cat = item['cat']
    total_price = item['price'] * item['qty']
    c_t[cat] = c_t.get(cat, 0) + total_price
    
for cat in sorted(c_t.keys()):
    print(cat, c_t[cat])