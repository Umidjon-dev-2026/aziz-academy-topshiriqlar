# Agar bo‘lishda b=0 bo‘lsa "Error" chiqaring.
parts = input().split()
a = int(parts[0])
b = int(parts[1])
tanlov = int(input())

if tanlov == 4:
    if b == 0:
        print("Error")
    else:
        print(a / b)
        
        