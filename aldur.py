n = int(input())
youngest = 100000
for i in range(n):
    age = int(input())
    if age < youngest:
        youngest = age
print(youngest)
