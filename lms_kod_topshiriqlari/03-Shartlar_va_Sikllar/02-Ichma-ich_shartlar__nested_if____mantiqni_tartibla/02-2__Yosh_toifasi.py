# age
# Agar age >= 18 bo'lsa:
#   agar age >= 60 bo'lsa "Senior"
#   aks holda "Adult"
# Aks holda "Minor"
age = int(input())
if age >= 18:
    if age >= 60:
         print("Senior")
    else:
         print("Adult")
else:
    print("Minor")

    