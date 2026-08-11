# Agar a yoki b manfiy bo‘lsa "Invalid" chiqaring.
parts = input().split()
a = int(parts[0])
b = int(parts[1])
tanlov = int(input())

if a < 0 or b < 0:
    print("Invalid")
elif tanlov == 1:
    print(a + b)
