n = int(input())
k = int(input())

if(k >= n):
    print("impossible")
else:
    for i in range(k):
        print("open", i+1, "using", i+2)
