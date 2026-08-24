# n = int(input())
# lst = list(map(int, input().split()))
# Faqat juft indexdagilarni qoldiring (0,2,4...) slicing bilan va listni chiqaring.
n = int(input())
x = list(map(int, input().split()))
print(x[::2])