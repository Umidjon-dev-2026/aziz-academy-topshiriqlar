# score
# Agar score >= 50 bo'lsa:
#   agar score >= 90 bo'lsa "Excellent"
#   aks holda "Pass"
# Aks holda "Fail"
s = int(input())
if s >= 50:
    if s >= 90:
        print("Excellent")
    else:
        print("Pass")
else:
    print("Fail")    