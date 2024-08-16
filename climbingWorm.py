n = input()
num = n.split(" ")
total = 0
count = 0
while total < int(num[2]):
    total = total + int(num[0])
    count = count + 1
    if(total < int(num[2])):
        total = total - int(num[1])
    else:
        break
    
print(count)
