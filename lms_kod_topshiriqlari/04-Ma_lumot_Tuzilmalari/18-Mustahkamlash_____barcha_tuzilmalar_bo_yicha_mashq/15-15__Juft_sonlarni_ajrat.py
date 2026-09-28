# Kodingizni shu yerga yozing
nums = list(map(int, input().split()))
juftlar = [x for x in nums if x % 2 == 0]
if juftlar:
    print(*(juftlar))
else:
    print("yo'q")