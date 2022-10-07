num = int(input())
for i in range(num):
    str3=""
    str1 = input()
    str2 = input()
    
    for j in range(len(str1)):
        if(str1[j]!=str2[j]):
            str3 += "*"
        else:
            str3 += "."

    print(str1)
    print(str2)
    print(str3)
