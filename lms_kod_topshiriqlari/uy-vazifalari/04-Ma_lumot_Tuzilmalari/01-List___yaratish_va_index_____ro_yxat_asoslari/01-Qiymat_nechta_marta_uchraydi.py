nums = input().split()
v = input()

sonlar = 0

for x in nums:
    if x == v:
        sonlar += 1
print(sonlar)