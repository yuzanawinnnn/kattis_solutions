num = int(input())
for i in range(num):
    temp = input().split(" ")
    if(int(temp[0])+int(temp[1])==int(temp[2])):
        print("Possible")
    elif(int(temp[0])-int(temp[1])==int(temp[2])):
        print("Possible")
    elif(int(temp[0])*int(temp[1])==int(temp[2])):
        print("Possible")
    elif(int(temp[0])/int(temp[1])==int(temp[2])):
        print("Possible")
    elif(int(temp[1])+int(temp[2])==int(temp[0])):
        print("Possible")
    elif(int(temp[1])-int(temp[2])==int(temp[0])):
        print("Possible")
    elif(int(temp[1])*int(temp[2])==int(temp[0])):
        print("Possible")
    elif(int(temp[1])/int(temp[2])==int(temp[0])):
        print("Possible")
    else:
        print("Impossible")
