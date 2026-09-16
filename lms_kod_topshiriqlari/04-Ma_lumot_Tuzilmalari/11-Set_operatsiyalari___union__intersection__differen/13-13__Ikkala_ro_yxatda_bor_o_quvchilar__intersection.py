# 2 qator: 2 ta ro‘yxat (ism-lar, space bilan)
# 1-qator: A guruh
# 2-qator: B guruh
# Ikkalasida ham borlarini toping.
# Output:
# 1-qator: soni
# Keyingi qatorlar: sort qilingan ismlar (har biri alohida qatorda)

A = set(input().strip().split())
B = set(input().strip().split())
# TODO
res = A & B 
print(len(res))
for name in sorted(res):
    print(name)