num = int(input())
name = []
love = []
birthday = []
for i in range(num):
    friend = input()
    friend = friend.split(" ")
    if(friend[2] not in birthday):
        name.append(friend[0])
        love.append(friend[1])
        birthday.append(friend[2])
    else:
        if(int(love[birthday.index(friend[2])])<int(friend[1])):
            name[birthday.index(friend[2])] = friend[0]
            love[birthday.index(friend[2])] = friend[1]
            birthday[birthday.index(friend[2])] = friend[2]
name.sort()
print(len(name))
for i in range(len(name)):
    print(name[i])
            
        
    
