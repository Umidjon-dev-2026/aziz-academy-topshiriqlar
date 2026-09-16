# 2 qator: 2 ta gap (matn)
# Har bir gapni split() qiling, so‘zlar unionini oling.
# Natija: unikal so‘zlar sonini chiqaring.
# Eslatma: katta-kichik farq qilmasin -> lower() ishlating.

s1 = set(input().strip().lower().split())
s2 = set(input().strip().lower().split())
# TODO
print(len(s1 | s2))