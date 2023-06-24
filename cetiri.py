arr = list(map(int,input().split(' ')))
arr.sort()
diff1 = arr[2]-arr[1]
diff2 = arr[1]-arr[0]
if(diff1 == diff2):
    print(arr[2]+diff1)
elif(diff1>diff2):
    print(arr[1]+diff2)
else:
    print(arr[0]+diff1)
    
