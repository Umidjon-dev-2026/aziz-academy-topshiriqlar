# s beriladi.
# for bilan yangi string yasang:
# 'a' bo‘lsa '@' ga almashtiring, aks holda o‘sha belgini qo‘shing.
# Natijani chiqaring.
s = input()
r = ""
for c in s:
    r += "@" if c == "a" else c 
print(r)