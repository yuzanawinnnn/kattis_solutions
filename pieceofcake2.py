num=input().split(" ")
n=int(num[0])
h=int(num[1])
v=int(num[2])

print(max(n-v,v)*max(n-h,h)*4)
