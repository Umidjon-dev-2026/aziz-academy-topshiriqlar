words = input().lower().split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
best_word = min(counts.keys(), key=lambda w: (-counts[w], w))
print(f"{best_word} {counts[best_word]}")