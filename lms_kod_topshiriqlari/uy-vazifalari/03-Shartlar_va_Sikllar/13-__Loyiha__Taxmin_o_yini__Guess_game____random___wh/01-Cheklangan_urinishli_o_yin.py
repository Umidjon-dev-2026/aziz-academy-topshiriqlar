yashirin_son = int(input())
n = int(input())

for i in range(n):
    taxmin = int(input())
    
    if taxmin == yashirin_son:
        print("TOPDINGIZ")
        break
    elif taxmin < yashirin_son:
        print("KICHIK")
    else:
        print("KATTA")
        
else:
    print("YUTQAZDINGIZ")