word = input()
for i in range(len(word)):
    if(len(word)-i>=2):
        if(word[i]==":" and word[i+1]==")"):
           print(i)
        elif(word[i]==";" and word[i+1]==")"):
           print(i)
    if(len(word)-i>=3):
        if(word[i]==":" and word[i+1]=="-" and word[i+2]==")"):
            print(i)
        elif(word[i]==";" and word[i+1]=="-" and word[i+2]):
            print(i)
