n = int(input())
arr = set()
for i in range(n):
    s = input()
    arr.add(s)
if(len(arr)>1):
    print("blandad best")
else:
    arr = list(arr)
    print(arr[0])
    
    
