# 2 qator beriladi:
# 1-qator: A set elementlari (bo‘sh joy bilan)
# 2-qator: B set elementlari
# Union (A ∪ B) ni toping va SORT qilingan holda chiqaring.
# Output: elementlar space bilan
# Misol: 1 2 2 3  -> set: {1,2,3}

a = set(map(int, input().split()))
b = set(map(int, input().split()))
# TODO
print(*(sorted(a | b)))