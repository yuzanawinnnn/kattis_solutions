n = int(input())
count = 0
while n > 1:
    if(n%2 != 0):
        n = n + n * 2 + 1
        count = count + 1
    if(n%2 == 0):
        n = n / 2
        count = count + 1
print(count)
        
    
