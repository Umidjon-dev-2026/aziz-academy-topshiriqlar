# s beriladi.
# for bilan unlilar (a,e,i,o,u) sonini hisoblang.
# (Faqat kichik harflar deb oling.)
s = input()
sa = 0
for belgi in s:
    if belgi in 'aeiou':
        sa += 1
print(sa)