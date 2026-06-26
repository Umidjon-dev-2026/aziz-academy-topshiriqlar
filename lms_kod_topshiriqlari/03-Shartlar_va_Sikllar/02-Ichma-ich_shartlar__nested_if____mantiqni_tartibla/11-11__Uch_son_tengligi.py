# a b c
# Agar a == b bo'lsa:
#   agar b == c bo'lsa "All equal"
#   aks holda "Partially equal"
# Aks holda "Not equal"
a, b, c = map(int, input().split())
if a == b:
    if b == c:
        print("All equal")
    else:
        print("Partially equal")
else:
    print("Not equal")