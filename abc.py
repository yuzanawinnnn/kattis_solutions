num = input()
num = num.split(" ")
num = list(map(int, num))
num.sort()
word = input()
s = ""
for i in range(len(word)):
    if(word[i]=="A"):
        s = s + str(num[0])+" "
    elif(word[i]=="B"):
        s = s + str(num[1])+" "
    else:
        s = s + str(num[2])+" "
print(s)
