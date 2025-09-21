n = int(input())
squirrels = 0

while n > 0:
    i = 1

    while True:
        if(pow(2,i)> n):
            j = i - 1
            squirrels = squirrels + 1
            break
        elif(pow(2,i) == n):
            j = i
            squirrels = squirrels + 1
            break
        else:
            i = i + 1
    n = n - pow(2, j)
    if(n < 2 and n > 0):
        squirrels = squirrels + 1
        break
        

print(squirrels)
