num = int(input())
vol=7
for i in range(num):
    temp=input().split(" ")
    if (temp[1]=="op!" and vol<10):
        vol += 1
    elif(temp[1]=="ned!" and vol>0):
        vol -=1
print(vol)
