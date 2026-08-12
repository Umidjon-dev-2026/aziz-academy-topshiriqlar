a = int(input())
b = int(input())

juft_sonlar = sum([i for i in range(a, b + 1) if i % 2 == 0])

print(juft_sonlar)