balance = 0
while True:
    cmd = input().strip()
    if cmd == 'exit':
        break
    parts = cmd.split()
    op = parts[0]
    if op == "deposit":
        balance += int(parts[1])
        print("Balans:", balance)