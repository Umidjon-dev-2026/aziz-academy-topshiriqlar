s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
try:
    _ = input()
except EOFError:
    pass
res = s1 - s2
if res:
    print(" ".join(str(x) for x in sorted(res)))
else:
    print("BO'SH")