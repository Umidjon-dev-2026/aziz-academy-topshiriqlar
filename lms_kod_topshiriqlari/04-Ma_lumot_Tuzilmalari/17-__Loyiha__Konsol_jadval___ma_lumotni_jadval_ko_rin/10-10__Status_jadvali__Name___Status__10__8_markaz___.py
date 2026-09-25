n = int(input())
for _ in range(n):
    name, flag = input().split()
    if flag == 1:
        status = "absent"
    else:
        status = "present"
    print("{}|{}".format(name, status))