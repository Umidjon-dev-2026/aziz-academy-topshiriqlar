# INPUT:
# n
# n qator: username active
# active: 1 yoki 0
# Vazifa: active=1 bo‘lganlar soni

n = int(input().strip())
users = []
for _ in range(n):
    username, active = input().split()
    users.append({'username': username, 'active': active == '1'})

# TODO
a_c = sum(1 for user in users if user['active'])
print(a_c)