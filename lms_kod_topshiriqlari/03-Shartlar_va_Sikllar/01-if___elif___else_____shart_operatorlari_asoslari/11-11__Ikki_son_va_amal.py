# a va b
# a>b bo'lsa a-b, aks holda a+b
a, b = map(int, input().split())
if a > b:
    print(a-b)
else:
    print(a+b)