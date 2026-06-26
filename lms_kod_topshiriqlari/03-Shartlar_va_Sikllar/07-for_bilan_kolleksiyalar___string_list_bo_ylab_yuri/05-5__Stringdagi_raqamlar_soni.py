# s beriladi.
# for bilan s ichidagi raqam (0-9) belgilar sonini chiqaring.
s = input()
sa = 0
for belgi in s:
    if belgi.isdigit():
        sa += 1
print(sa)