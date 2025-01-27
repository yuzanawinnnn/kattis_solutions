arr = []
for i in range(3):
    s = input().split(" ")
    arr.append(s)

win = False

for i in range(3):

    if(arr[i][0] == arr[i][1] == arr[i][2] and arr[i][0] != "_"):
        if(arr[i][0] == "X"):
            print("Johan har vunnit")
        else:
            print("Abdullah har vunnit")
        win = True
        break
    elif(arr[0][i] == arr[1][i] == arr[2][i] and arr[0][i] != "_"):
        if(arr[0][i] == "X"):
            print("Johan har vunnit")
        else:
            print("Abdullah har vunnit")
        win = True
        break
if(arr[0][0] == arr[1][1] == arr[2][2] and arr[0][i] != "_"):
    if(arr[0][i] == "X"):
        print("Johan har vunnit")
    else:
        print("Abdullah har vunnit")
    win = True

elif(arr[0][2] == arr[1][1] == arr[2][0] and arr[0][i] != "_"):
    if(arr[0][i] == "X"):
        print("Johan har vunnit")
    else:
        print("Abdullah har vunnit")
    win = True
        
    
if (win == False):
    print("ingen har vunnit")
        
   
    
