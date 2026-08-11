# Ikki son va tanlov beriladi.
# Agar tanlov 1 bo‘lsa, a+b ni chiqaring.
parts = input().split()
a = int(parts[0])
b = int(parts[1])
tanlov = int(input())

if tanlov == 1:
    print(a + b)