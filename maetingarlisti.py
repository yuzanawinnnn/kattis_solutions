num = input()
num = num.split(" ")

row = []

for i in range(int(num[1])):
    r = input()
    r = r.split(" ")
    row.append(r[0])
    
for j in range(int(num[1])):
    for k in range(int(num[2])):
        name = input()
    if(name in row):
        print("right")
    else:
        print("left")
    
