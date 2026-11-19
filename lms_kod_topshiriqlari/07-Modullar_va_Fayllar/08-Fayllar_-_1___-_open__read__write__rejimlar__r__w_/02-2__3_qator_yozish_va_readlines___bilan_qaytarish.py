a = input()
b = input()
c = input()
f = open("task2.txt", "w")
f.write(a + "\n" + b + "\n" + c + "\n")
f.close()
f = open("task2.txt", "r")
qatorlar = f.readlines()
f.close()
print(len(qatorlar))
for q in qatorlar:
    print(q.rstrip("\n"))
    