def power(a, b):
    return a ** b 
qator = list(map(int, input().split()))
a = qator[0]
b = qator[1]
print(power(a, b))
print(power(b=b, a=a))