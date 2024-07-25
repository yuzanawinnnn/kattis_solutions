room = []
n = input()
n = n.split(" ")
for i in range(int(n[1])):
    room_no = int(input())
    room.append(room_no)
if(int(n[0]) == int(n[1])):
    print("too late")
else:
    for j in range(1, int(n[0])+1):
        if(j not in room):
            print(j)
            break
    
    
