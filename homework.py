line = input()
arr = line.split(";")
count =0
for i in range(len(arr)):
    if("-" not in arr[i]):
        count = count +1
    else:
        a,b=arr[i].split("-")
        ans = int(b)-int(a)+1
        count= count+ ans
print(count)
