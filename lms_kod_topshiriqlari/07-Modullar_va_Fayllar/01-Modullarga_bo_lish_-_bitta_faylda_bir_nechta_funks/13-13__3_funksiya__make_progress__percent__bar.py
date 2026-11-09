def percent(done, total):
    if total <= 0:
        return 0
    p = done * 100 // total
    return max(0, min(100, p))
def bar(p):
    n = p // 10
    return "%" * n + "." * (10 - n)

def make_progress(done, total):
    p = percent(done, total)
    return str(p) + "% " + bar(p)

done, total = map(int, input().split())
print(make_progress(done, total))