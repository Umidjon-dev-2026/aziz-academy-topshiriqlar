# Yashirin son = 15
# Agar farq >5 bo‘lsa "Far", aks holda "Close", teng bo‘lsa "Correct".
yashirin_son = 15
while True:
    x = int(input())
    if x == yashirin_son:
        print("Correct")
        break
    elif abs(x - yashirin_son) >= 5:
        print("Far")
    else:
        print("Close")