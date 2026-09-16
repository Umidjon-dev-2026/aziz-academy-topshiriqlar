# N ta mahsulot
# Eng arzon mahsulot nomini chiqaring

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
# TODO
a = min(products, key=lambda x: x['price'])
print(a['name'])