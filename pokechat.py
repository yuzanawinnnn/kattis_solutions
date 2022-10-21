word = input()
num  = input()
temp=0
ss =""
for i in range(1,len(num)):
    if((i+1)%3==0):
        ss+=word[int(num[temp:i+1])-1]
        temp =i+1

print(ss)
