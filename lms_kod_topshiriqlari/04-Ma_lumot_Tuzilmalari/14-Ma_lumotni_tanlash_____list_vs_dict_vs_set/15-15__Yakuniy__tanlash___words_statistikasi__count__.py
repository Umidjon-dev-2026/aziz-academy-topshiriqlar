words = input().lower().split()
total_count = len(words)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
a = len(counts)
top_word = min(counts.keys(), key=lambda w: (-counts[w], w))
print(f"total: {total_count}")
print(f"unique: {a}")
print(f"top: {top_word} {counts[top_word]}")