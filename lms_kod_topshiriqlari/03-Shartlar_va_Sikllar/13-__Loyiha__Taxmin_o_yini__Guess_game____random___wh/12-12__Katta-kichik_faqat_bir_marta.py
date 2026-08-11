# Yashirin son = 8
# Birinchi urinishda faqat yordam beriladi.
# Keyingisida faqat Correct yoki Wrong.
yashirin_son = 8
first = True
while True:
    x = int(input())
    if x == yashirin_son:
        print("Correct")
        break
    if first:
        if x < yashirin_son:
            print("Low")
        else:
            print("High")
        first = False
    else:
        print("Wrong")