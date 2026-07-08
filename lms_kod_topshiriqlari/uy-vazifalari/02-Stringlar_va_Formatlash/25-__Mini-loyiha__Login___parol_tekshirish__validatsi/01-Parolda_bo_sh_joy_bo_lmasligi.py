s = input()
print(" " not in s and any(c.isdigit() for c in s))