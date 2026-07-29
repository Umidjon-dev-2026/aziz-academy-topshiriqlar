# n beriladi.
# n dan kichik bo‘lgan eng katta bo‘luvchini toping.
# Agar yo‘q bo‘lsa, 0 chiqaring.
n = int(input())
s = 0
for i in range(1, n):
    if n % i == 0:
        s = i 
print(s)