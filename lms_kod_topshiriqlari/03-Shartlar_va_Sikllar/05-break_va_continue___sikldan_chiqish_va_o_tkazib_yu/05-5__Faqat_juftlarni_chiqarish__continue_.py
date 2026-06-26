# n beriladi.
# 1..n oralig‘ida faqat juft sonlarni chiqar.
# Toq bo‘lsa continue ishlat.
n =int(input())
i = 1 
while i <= n:
    if i % 2 != 0:
        i += 1
        continue
    print(i)
    i += 1