number = input()
n = number.split(" ")

luggage = input()
l_arr = luggage.split(" ")

for i in range(len(l_arr)):
    if l_arr[0] == n[1]:
        print("fyrst")
        break
    elif l_arr[1] == n[1]:
        print("naestfyrst")
        break
    elif l_arr[i] == n[1]:
        print(i+1,"fyrst")
        break
    
    
