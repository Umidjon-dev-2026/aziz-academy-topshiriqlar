# Yashirin son = 8
# Foydalanuvchiga maksimal 3 ta urinish beriladi.
# Agar topa olmasa "Game Over" chiqaring.
yashirin_son = 8
urinish = 0
found = False
while urinish < 3:
    x = int(input())
    urinish += 1
    if x == yashirin_son:
        print("Correct")
        found = True
        break
if not found:
    print("Game Over")