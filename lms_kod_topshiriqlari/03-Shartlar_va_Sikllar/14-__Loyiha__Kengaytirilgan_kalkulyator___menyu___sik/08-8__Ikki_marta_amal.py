# Ikki marta menyu ishlasin.
# Har safar amal natijasini chiqaring.
while True:
    n = input()
    if n.strip() == "0":
        print("Exit")
        break
        
    parts = n.split()
    a = int(parts[0])
    b = int(parts[1])
    tanlov = int(input())
    
    if tanlov == 1:
        print(a + b)
    elif tanlov == 2:
        print(a - b)
    elif tanlov == 3:
        print(a * b)
    elif tanlov == 4:
        print(a / b)