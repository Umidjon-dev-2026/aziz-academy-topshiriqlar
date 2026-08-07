# n beriladi.
# Agar bo‘luvchilari soni 2 dan ko‘p bo‘lsa "Yes", aks holda "No" chiqaring.
n = int(input())
c = 0
for i in range(1, n + 1):
    if n % i == 0:
        c += 1
if c > 2:
    print("Yes")
else:
    print("No")