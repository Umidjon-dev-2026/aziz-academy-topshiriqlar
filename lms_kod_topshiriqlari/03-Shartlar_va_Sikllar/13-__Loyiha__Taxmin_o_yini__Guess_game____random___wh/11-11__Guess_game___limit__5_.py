# Yashirin son = 10
# 5 ta urinish beriladi.
# Oxirida yutqazsa "You lost" chiqaring.
yashiri_son = 10
urinish = 0
found = False
while urinish < 5:
    x = int(input())
    urinish += 1
    if x == yashiri_son:
        print("Correct")
        found = True
        break
if not found:
    print("You lost")