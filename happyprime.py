n = int(input())

for i in range(n):
    s = input()
    s = s.split(" ")
    
    
    if(int(s[1]) == 1):
        print(int(s[0]),int(s[1]),"NO")
    elif(int(s[1]) < 7):
        print(int(s[0]),int(s[1]),"NO")
    elif(int(s[1]) > 1 and all(int(s[1]) % m for m in range(2, int(int(s[1])**0.5) + 1))):
        num = s[1]
        while True:
            total = 0
            for j in range(len(num)):
                total = total + int(num[j]) *int(num[j])
            if(total == 1):
                print(int(s[0]),int(s[1]),"YES")
                break
            elif(total < 7):
                print(int(s[0]),int(s[1]),"NO")
                break
            
            num = str(total)
    else:
        print(int(s[0]),int(s[1]),"NO")
            


            
            happyprime.py
