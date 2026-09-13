# Kodingizni shu yerga yozing
n = int(input())
a = []

for i in range(n):
    a.append(input())
javob = a[0]

for soz in a:
    if a.count(soz) > a.count(javob):
        javob = soz
print(javob)