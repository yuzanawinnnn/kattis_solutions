a, b = map(int,input().split(' '))
A = max(a,b)
B = min(a,b)
if B == 0:
    print(A)
else: 
    C = A % B
    if (C == 0):
        print(B)
    elif(C == 1):
        print(1)
    else: 
        while True and C>0:
            temp =  B % C
            if(temp == 0):
                print(C)
                break
            else: 
                B = C
                C = temp
