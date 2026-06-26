# role
# admin -> "Full access"
# user -> "Limited"
# aks holda "Guest"
x = input().strip().lower()
if x == "admin":
    print("Full access")
elif x == "user":
    print("Limited")
else:
    print("Guest")
