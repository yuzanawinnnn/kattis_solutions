price = int(input())
coins = [150, 30, 15, 5, 1]
count = [0, 0, 0, 0, 0]

i = 0
while price > 0:
    if(price < coins[i]):
        i = i + 1
    else:
        price = price - coins[i]
        count[i] = count[i] + 1
count = count[::-1]
s = ""
for j in range(len(count)):
    s = s + str(count[j]) + " "
print(s)
    
