# n = int(input())
# lst = list(map(int, input().split()))
# Birinchi va oxirgi elementni joyini almashtiring va listni chiqaring.
n = int(input())
lst = list(map(int, input().split()))
a = lst[0]
lst[0] = lst[-1]
lst[-1] = a 
print(lst)