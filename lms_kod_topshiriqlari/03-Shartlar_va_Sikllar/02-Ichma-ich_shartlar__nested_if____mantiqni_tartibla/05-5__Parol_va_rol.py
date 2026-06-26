# password
# Agar password == "1234" bo'lsa:
#   agar password == "1234" bo'lsa "Admin"
# Aks holda "Denied"
password = input()
if password == "1234":
    print("Admin")
else:
    print("Denied")