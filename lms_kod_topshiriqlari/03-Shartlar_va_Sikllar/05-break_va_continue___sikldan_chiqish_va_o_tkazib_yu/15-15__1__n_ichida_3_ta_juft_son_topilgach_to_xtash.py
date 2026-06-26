# n beriladi.
# while bilan 1..n yurib, juft sonlarni sanang.
# 3 ta juft son topilishi bilan break qiling.
# Nechanchi son (i) da to‘xtaganingizni chiqaring.
# Agar 3 ta juft son topilmasa, "No" chiqaring.
n = int(input())
i = 1
count = 0
while i <= n:
    if i % 2 == 0:
        count += 1
        if count == 3:
            print(i)
            break
    i += 1
if count < 3:
    print("No")