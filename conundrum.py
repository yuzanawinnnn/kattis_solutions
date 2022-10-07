word = input()
j=0.    
count=0 #count the word changes
num = int(len(word)/3) 

for i in range(num):
    temp=word[j:j+3]
    if(temp[0]!="P"):
        count+=1
    if(temp[1]!="E"):
        count+=1
    if(temp[2]!="R"):
        count+=1
    j+=3
print(count)
        
