count = 0
while True:
    n = int(input())
    if(n == 0):
        break
    count = count + 1
    print("SET", count)
    top = []
    bottom = []

    for i in range(1,n+1):
        name = input()
        if(i%2 != 0):
            top.append(name)
        else:
            bottom.append(name)

    final = top + bottom [::-1]
    for j in range(n):
        print(final[j])

    
