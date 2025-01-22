s = input()
s = s.split(" ")
arr = []
count = 0
for i in range(int(s[0])):
    z = input()
    z = list(z)
    arr.append(z)

    
for j in range(1,int(s[0])-1):
    for k in range(1,int(s[1])-1):
        if(arr[j][k] == "0"):
            if(arr[j][k-1] == "O" and arr[j][k+1] == "O" and arr[j-1][k-1] == "O" and arr[j-1][k] == "O" and arr[j-1][k+1] == "O" and arr[j+1][k-1] == "O" and arr[j+1][k] == "O" and arr[j+1][k+1] == "O"):
                count = count + 1
                if(count == 1):
                    loc = str(j+1) + " " + str(k+1)
if(count == 0):
    print("Oh no!")
elif(count == 1):
    print(loc)
else:
    print("Oh no!", count,"locations")
            

    
    
