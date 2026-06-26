# price
# Agar price >= 100 bo'lsa:
#   agar price >= 500 bo'lsa 20% chegirma
#   aks holda 10% chegirma
# Aks holda price o'zgarishsiz
price = int(input())
if price >= 100:
    if price >= 500:
        print(price * 0.8)
    else:
        print(price * 0.9)
else:
    print(price)