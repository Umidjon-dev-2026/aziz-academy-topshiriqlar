# age
# 1 -> Adult (>=18)
# 2 -> Minor (<18)
# aks holda Invalid
age = int(input())
if age == 1:
    print("Adult")
elif age == 2:
    print("Minor")
else:
    print("Invalid")