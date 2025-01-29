n = int(input())
total = 0


for i in range(1,n+1):
    gift = 0
    for j in range(1,i+1):
        gift = gift + j
    total = total + gift

print(gift)
print(total)
