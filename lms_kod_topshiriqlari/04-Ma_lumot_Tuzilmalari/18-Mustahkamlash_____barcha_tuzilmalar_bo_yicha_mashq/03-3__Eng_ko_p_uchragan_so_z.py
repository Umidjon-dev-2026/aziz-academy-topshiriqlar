# Kodingizni shu yerga yozing
words = input().split()
cnt = {}
for word in words:
    cnt[word] = cnt.get(word, 0) + 1
print(max(cnt, key=cnt.get))