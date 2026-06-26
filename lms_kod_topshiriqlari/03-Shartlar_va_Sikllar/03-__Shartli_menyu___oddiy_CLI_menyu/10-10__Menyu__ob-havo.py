# weather
# sunny -> "Go out"
# rainy -> "Stay home"
# aks holda "Unknown"
w = input().strip().lower()
if w == "sunny":
    print("Go out")
elif w == "rainy":
    print("Stay home")
else:
    print("Unknown")