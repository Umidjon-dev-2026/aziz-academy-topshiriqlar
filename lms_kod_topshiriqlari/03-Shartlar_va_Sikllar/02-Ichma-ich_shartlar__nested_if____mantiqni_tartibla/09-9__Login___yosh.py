# username va age
# Agar username == "admin" bo'lsa:
#   agar age >= 18 bo'lsa "Full access"
#   aks holda "Limited"
# Aks holda "No access"
username, age = input().split()
age = int(age)
if username == "admin":
    if age >= 18:
        print("Full access")
    else:
        print("Limited")
else:
    print("No access")    