# To‘liq menyu tuzing: 1..6 amallar, 0 chiqish.
# while + if/elif/else ishlating.

while True:
    line = input()
    if line.strip() == "0":
        print("Exit")
        break
    
    parts = line.split()
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
    elif tanlov == 5:
        print(a % b)
    elif tanlov == 6:
        print(a ** b)