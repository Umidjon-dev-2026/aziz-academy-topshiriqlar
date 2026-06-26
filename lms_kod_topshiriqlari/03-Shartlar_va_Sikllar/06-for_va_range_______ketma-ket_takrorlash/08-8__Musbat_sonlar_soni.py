# n beriladi.
# 1..n oralig‘ida nechta musbat son borligini for bilan hisobla.
n = int(input())
sanoq = 0 
for i in range(1, n + 1):
    if i > 0:
        sanoq += 1
print(sanoq)