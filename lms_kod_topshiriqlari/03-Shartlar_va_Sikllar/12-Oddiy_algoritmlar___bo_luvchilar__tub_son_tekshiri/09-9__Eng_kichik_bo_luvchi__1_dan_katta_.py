# n beriladi.
# 1 dan katta eng kichik bo‘luvchini toping.
# Agar bo‘lmasa (n=1), 0 chiqaring.
n = int(input())
found = True
for i in range(2, n + 1):
    if n % i == 0:
        print(i)
        found = False
        break
if found:
    print(0)