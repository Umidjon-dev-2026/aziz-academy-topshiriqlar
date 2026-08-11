# Ikki son va tanlov beriladi.
# Agar tanlov 4 bo‘lsa, a/b ni chiqaring.
parts = input().split()
a = int(parts[0])
b = int(parts[1])
tanlov = int(input())

if tanlov == 4:
    print(a / b)