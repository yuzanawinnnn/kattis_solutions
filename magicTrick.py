line = input()
found = False
i = 0
while found == False and i<len(line):
    if(line.count(line[i]) >1):
        found = True
    i = i +1
if(found == False):
    print(1)
else:
    print(0)
