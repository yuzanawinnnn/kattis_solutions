num = int(input())
for i in range(num):
    temp = input()
    if("Simon says" in temp):
        s= temp.index("says")+5
        print(temp[s:])
