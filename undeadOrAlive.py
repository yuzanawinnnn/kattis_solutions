line = input()
smile = False
frown = False
for i in range(len(line)-1):
    if(line[i] ==":" and line[i+1]==")"):
        smile = True
    elif (line[i] ==":" and line[i+1]=="("):
        frown = True
if(smile and frown):
    print("double agent")
elif(smile):
    print("alive")
elif(frown):
    print("undead")
else:
    print("machine")
