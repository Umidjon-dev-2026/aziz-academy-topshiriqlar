# a va b
# Agar a == b bo'lsa:
#   agar a == 0 bo'lsa "Equal Zero"
#   aks holda "Equal"
# Aks holda "Not equal"
a, b = map(int, input().split())
if a == b and a == 0:
    print("Equal Zero")
elif a == b:
    print("Equal")
else:
    print("Not equal")