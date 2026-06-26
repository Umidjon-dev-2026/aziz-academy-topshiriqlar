# a va b beriladi.
# for + range yordamida a dan b gacha yig‘indini hisobla.
# (a <= b deb hisoblang)
a, b = map(int, input().split())
yigindi = 0
for i in range(a, b + 1):
    yigindi += i
print(yigindi)