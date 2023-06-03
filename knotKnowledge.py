n = int(input())
line1 = input()
arr1 = line1.split(" ")
line2 = input()
arr2 = line2.split(" ")
for i in range(len(arr1)):
    if(arr1[i] not in arr2):
        print(arr1[i])
