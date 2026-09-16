# N ta mahsulot
# Mahsulotlarni narx bo‘yicha o‘sish tartibida chiqarish
# Har qator: name price

n = int(input())
products = []
for _ in range(n):
    name, price = input().split()
    products.append({'name': name, 'price': int(price)})
products.sort(key=lambda x: x['price'])
for p in products:
    print(f"{p['name']} {p['price']}")