# n beriladi.
# for bilan 1..n ichida 3 ga karrali sonlar sonini chiqaring.
n = int(input())
sanoq = 0
for i in range(1, n + 1):
    if i % 3 == 0:
        sanoq += 1
print(sanoq)