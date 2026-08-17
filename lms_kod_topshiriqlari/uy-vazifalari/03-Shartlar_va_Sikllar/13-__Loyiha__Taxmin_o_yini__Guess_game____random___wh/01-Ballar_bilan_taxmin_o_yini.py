yashirin_son = int(input())
ball = 100

while True:
    taxmin = int(input())
    
    if taxmin > yashirin_son:
        print("KATTA")
        ball -= 10
        if ball < 0:
            ball = 0
            
    elif taxmin < yashirin_son:
        print("KICHIK")
        ball -= 10
        if ball < 0:
            ball = 0
    else:
        print("TOPDINGIZ")
        break
            
print(f"Ball: {ball}")