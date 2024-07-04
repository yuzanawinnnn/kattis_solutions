n = int(input())
seven = ""
for i in range(3):
    num = input()
    digit = num.split(" ")
    if '7' in digit:
        seven = seven + "T"
    else:
        print(0)
        break
if(seven == "TTT"):
    print(777)
        
