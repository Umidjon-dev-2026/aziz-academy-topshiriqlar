# Yashirin son = -4
# Katta/kichik tekshiruvi manfiy sonlar bilan ham ishlasin.4
yashirin_son = -4
while True:
    x = int(input())
    if x == yashirin_son:
        print("Correct")
        break
    elif x < yashirin_son:
        print("Low")
    else:
        print("High")