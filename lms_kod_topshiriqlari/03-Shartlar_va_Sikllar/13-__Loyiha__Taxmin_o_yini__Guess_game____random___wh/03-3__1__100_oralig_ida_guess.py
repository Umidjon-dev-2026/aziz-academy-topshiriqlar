# Yashirin son = 42
# Kiritilgan son kichik bo‘lsa "Low", katta bo‘lsa "High", teng bo‘lsa "Correct".
yashirin_son = 42
while True:
    x = int(input())
    if x < yashirin_son:
        print("Low")
    elif x > yashirin_son:
        print("High")
    else:
        print("Correct")
        
        break