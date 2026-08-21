# lst = [1, 2, 3]
# x beriladi.
# Agar x listda bo‘lsa remove qiling va "Removed" chiqaring.
# Aks holda "Not found" chiqaring.
# Oxirida listni ham chiqaring.
list = [1, 2, 3]
x = int(input())
if x in list:
    list.remove(x)
    print("Removed")
else:
    print("Not found")

print(list)