# price
# <50 -> Cheap
# <200 -> Medium
# aks holda Expensive
p = int(input())
if p < 50:
    print("Cheap")
elif p < 200:
    print("Medium")
else:
    print("Expensive")