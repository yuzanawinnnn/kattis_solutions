line = input()
arr = []
count ={'P':13,'K':13,'H':13,'T':13}
flag = False
i= 0
s = ""
while flag == False and i<len(line):
    if(line[i:i+3] not in arr):
        arr.append(line[i:i+3])
        count[line[i]] = count[line[i]] - 1
    else:
        print("GRESKA")
        flag = True
    i = i + 3
if(flag != True):
    for values in count.values():
        s = s + str(values) + " "
    print(s)
    
    
    
