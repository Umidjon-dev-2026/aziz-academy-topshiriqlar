# hour
# <12 -> Morning
# <18 -> Day
# aks holda Night
h = int(input())
if h < 12:
    print("Morning")
elif h < 18:
    print("Day")
else:
    print("Night")