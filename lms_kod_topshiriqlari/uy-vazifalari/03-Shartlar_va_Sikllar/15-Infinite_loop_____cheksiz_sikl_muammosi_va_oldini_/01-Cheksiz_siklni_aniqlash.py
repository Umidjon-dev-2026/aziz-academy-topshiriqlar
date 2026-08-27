start = int(input())
step = int(input())

if step <= 0:
    print("CHEKSIZ")
else:
    qadamlar_soni = 0
    qiymat = start
    while qiymat < 100:
        qiymat += step
        qadamlar_soni += 1
        
    print(qadamlar_soni)