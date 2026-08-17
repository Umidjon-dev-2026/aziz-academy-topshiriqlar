r = int(input())

total = 0
eng_yaxshi = 0

for i in range(1, r + 1):
    yashirin = int(input())
    urinish = 0
    
    while True:
        taxmin = int(input())
        urinish += 1
        
        if taxmin == yashirin:
            break
            
    print(f"Round {i}: {urinish} urinish")
    
    total += urinish
    
    if i == 1 or urinish < eng_yaxshi:
        eng_yaxshi = urinish
        
print(f"Jami: {total}")
print(f"Eng yaxshi: {eng_yaxshi}")