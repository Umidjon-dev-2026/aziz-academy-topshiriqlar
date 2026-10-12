def rect_area(w, h):
    return w * h
qator = list(map(int, input().split()))
w = qator[0]
h = qator[1]
print(rect_area(w, h))
print(rect_area(h=h, w=w))