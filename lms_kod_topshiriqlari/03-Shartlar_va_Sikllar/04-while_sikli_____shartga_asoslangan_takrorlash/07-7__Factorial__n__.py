# n beriladi.
# while yordamida n! (factorial) ni hisoblab chiqar.
# Masalan: 5! = 120
n = int(input())
f = 1
i = 1 
while i <= n:
    f *= i
    i += 1
print(f)