# t
# Agar t > 0 bo'lsa:
#   agar t > 30 bo'lsa "Hot"
#   aks holda "Warm"
# Aks holda "Cold"
t = int(input())
if t > 0:
    if t > 30:
        print("Hot")
    else:
        print("Warm")
else:
    print("Cold")