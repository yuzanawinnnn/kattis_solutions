n = int(input())
count = 0
for i in range(1,n):
    product = i * (i+1) * (i+2)
    if(product < n):
        count = count + 1
    else:
        break
print(count)
            
