n = input()
num = n.split(" ")
name = []
initial_list = []
for i in range(int(num[0])):
    temp = input()
    name.append(temp)
    split_name = temp.split(" ")
    initial_list.append(split_name[0][0] + split_name[1][0])
for j in range(int(num[1])):
    initial = input()
    if(initial in initial_list):
        if(initial_list.count(initial) > 1):
            print("ambiguous")
        else:
            print(name[initial_list.index(initial)])
    else:
        print("nobody")


    
    
    
