# Yashirin son = 1
# Har urinishda faqat "Try again" yoki "Correct" chiqaring.
# Urinishlar sonini oxirida chiqaring.
yashirin_son = 1
urinish = 0
while True:
    x = int(input())
    urinish += 1
    if x == yashirin_son:
        print("Correct")
        break
    else:
        print("Try again")
print(urinish)