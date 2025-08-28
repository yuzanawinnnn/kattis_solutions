n = list(map(int, input().split(" ")))
numbers = n[:3]
product = 1
for num in numbers:
    product *= num
print("COZY" if product == n[3] else "SO MUCH SPACE" if product > n[3] else "TOO TIGHT")
