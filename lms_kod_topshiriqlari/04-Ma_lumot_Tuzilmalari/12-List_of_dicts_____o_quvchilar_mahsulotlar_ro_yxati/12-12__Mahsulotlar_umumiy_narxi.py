# N ta mahsulot
# Umumiy narxni chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})

a = sum(p['price'] for p in products)
print(a)