line1 = input()
line2 = input()
line = line1+line2
arr =[]
for i in range(len(line)):
    arr.append(line[i])
arr.sort()
s =""
for j in range(len(arr)):
    s = s + arr[j]
print(s)
