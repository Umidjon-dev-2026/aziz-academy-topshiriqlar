son = int(input())
urinish = int(input())

for i in range(urinish):
    taxmin = int(input())
    
    if taxmin < son:
        print("KICHIK")
    elif taxmin > son:
        print("KATTA")
    else:
        print("TOPDINGIZ")