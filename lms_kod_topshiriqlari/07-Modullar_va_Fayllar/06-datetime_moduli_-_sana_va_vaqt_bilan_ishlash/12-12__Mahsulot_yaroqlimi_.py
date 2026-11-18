from datetime import date, timedelta
made = date.fromisoformat(input().strip())
n = int(input())
today = date.fromisoformat(input().strip())
last = made + timedelta(days=n)
print(last)
if today <= last:
    print("YAROQLI")
else:
    print("ESKIRGAN")