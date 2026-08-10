# Yashirin son = 6
# Agar foydalanuvchi 1..10 dan tashqari son kiritsa "Invalid" chiqaring (urinish sanalmaydi).
yashirin_son = 6
while True:
    x = int(input())
    if x < 1 or x > 10:
        print("Invalid")
        continue
    if x == yashirin_son:
        print("Correct")
        break