a = input()
s = 0
for i in a:
    if i in "aeiouAEIOU":
        s += 1
print(s)