word=input()
s1=word[0]
for i in range(1,len(word)):
    if(word[i]!=word[i-1]):
        s1+=word[i]
print(s1)
