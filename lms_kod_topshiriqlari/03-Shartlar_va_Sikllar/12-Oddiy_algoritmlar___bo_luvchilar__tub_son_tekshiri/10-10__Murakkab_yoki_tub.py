# n beriladi.
# Agar n tub bo‘lsa "Prime", aks holda "Not Prime" chiqaring.
n = int(input())
if n < 2:
    print("Not Prime")
else:
    tub = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tub = False
    if tub:
        print("Prime")
    else:
        print("Not Prime")