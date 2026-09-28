# Kodingizni shu yerga yozing
n = int(input())
product = []
for _ in range(n):
    name = input().strip()
    price = int(input().strip())
    product.append({"nom": name, "narx": price})
    
max_product = max(product, key=lambda d: d["narx"])
print(max_product["nom"])