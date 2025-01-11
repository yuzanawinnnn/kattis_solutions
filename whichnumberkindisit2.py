import math
T = int(input())
for i in range(T):
    N = int(input())
    s = math.sqrt(N)
    if(N%2 != 0):
        if(s.is_integer()):
            print("OS")
        else:
            print("O")
    elif(s.is_integer()):
        print("S")
    else:
        print("EMPTY")
