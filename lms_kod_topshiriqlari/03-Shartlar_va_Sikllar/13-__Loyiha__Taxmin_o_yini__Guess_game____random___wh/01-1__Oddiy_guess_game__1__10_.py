# Yashirin son = 7
# Foydalanuvchi son kiritadi.
# Agar kichik bo‘lsa "Low", katta bo‘lsa "High", teng bo‘lsa "Correct" chiqar va to‘xtat.
yashirin_son = 7
while True:
    n = int(input())
    
    if yashirin_son > n:
        print("Low")
    elif yashirin_son < n:
        print("High")
    else:
        print("Correct")
        
        break