# Yashirin son = 3
# Agar foydalanuvchi 0 kiritsa o‘yin tugasin va "Exit" chiqsin.
yashirin_son = 3
while True:
    x = int(input())
    if x == 0:
        print("Exit")
        break
    elif x == yashirin_son:
        print("Correct")
        break
    elif x < yashirin_son:
        print("Low")
    else:
        print("High")