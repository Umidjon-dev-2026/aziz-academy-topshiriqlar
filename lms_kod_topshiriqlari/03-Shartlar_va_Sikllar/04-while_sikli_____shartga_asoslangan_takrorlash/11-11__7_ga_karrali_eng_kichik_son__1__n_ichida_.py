# n beriladi.
# while yordamida 1..n ichida 7 ga karrali eng kichik sonni top.
# Agar topilmasa, "No" chiqarsin.
n = int(input())
i = 1
while i <= n:
    if i % 7 == 0:
        print(i)
        break
    i += 1
else:
    print("No")