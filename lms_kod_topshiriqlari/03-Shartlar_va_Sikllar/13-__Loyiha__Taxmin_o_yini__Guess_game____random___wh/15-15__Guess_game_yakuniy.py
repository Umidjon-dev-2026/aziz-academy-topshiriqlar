# Yashirin son = 20
# 1..20 oralig‘ida
# Low/High/Correct
# Urinishlar sonini sanang va oxirida chiqaring.
yashirin_son = 20
urinish = 0
while True:
    x = int(input())
    urinish += 1
    if x < 1 or x > 20:
        print("Invalid")
    elif x == yashirin_son:
        print("Correct")
        break
    elif x < yashirin_son:
        print("Low")
    else:
        print("High")
print(urinish)