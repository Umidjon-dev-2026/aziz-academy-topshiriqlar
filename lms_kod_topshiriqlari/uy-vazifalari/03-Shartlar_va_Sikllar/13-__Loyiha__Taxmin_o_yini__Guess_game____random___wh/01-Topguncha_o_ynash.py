yashirin = int(input())
urinish = 0
while True:
    x = int(input())
    urinish += 1
    
    if yashirin < x:
        print("KATTA")
    elif yashirin > x:
        print("KICHIK")
    else:
        print("TOPDINGIZ")
        print(f"Urinishlar: {urinish}")
        break