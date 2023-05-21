line = input()
name = {}
arr = []
while(line != '***'):
    if(line not in name):
        name[line] = 1
    else:
        name[line] = name[line] +1
    line = input()

for person, count in name.items():  
    if count == max(name.values()):
        arr.append(person)
if(len(arr) > 1):
    print("Runoff!")
else:
    print(arr[0])
