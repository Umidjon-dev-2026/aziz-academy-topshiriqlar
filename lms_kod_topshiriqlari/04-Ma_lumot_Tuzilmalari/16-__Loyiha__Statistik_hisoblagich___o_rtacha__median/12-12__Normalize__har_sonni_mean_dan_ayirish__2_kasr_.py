numbers = list(map(int, input().split()))
mean_val = sum(numbers) / len(numbers)
ruselt = [f"{x - mean_val:.2f}" for x in numbers]
print(" ".join(ruselt))