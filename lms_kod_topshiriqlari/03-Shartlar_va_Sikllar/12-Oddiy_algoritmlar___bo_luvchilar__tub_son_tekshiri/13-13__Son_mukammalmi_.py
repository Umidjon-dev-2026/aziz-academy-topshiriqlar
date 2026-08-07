# n beriladi.
# Agar n mukammal son bo‘lsa "Perfect", aks holda "Not Perfect" chiqaring.
# Mukammal son: o‘zidan tashqari bo‘luvchilar yig‘indisi n ga teng.
n = int(input())
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print("Perfect")
else:
    print("Not Perfect")
        